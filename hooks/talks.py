"""Fill in the Talks overview page at build time.

Counts entries on talks/talks.md, talks/workshops.md and talks/tutorials.md and
lists the most recent ones, so the overview stays correct when new talks are added.
Each entry is a list item that starts with "- **Title**" and has its date in
*italics* on the last line, e.g.:

- **Talk title**  
  Event, Venue  
  *18 February 2026*
"""
import os, re, datetime, logging

log = logging.getLogger("mkdocs.hooks.talks")
MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], 1)}
SOURCES = [("talks.md", "Invited talk", "talks/"), ("workshops.md", "Workshop", "talks/workshops/"),
           ("tutorials.md", "Tutorial", "talks/tutorials/")]


def _date(text):
    m = re.search(r"(?:(\d{1,2})(?:\s*[-–]\s*\d{1,2})?\s+)?([A-Za-z]+)\s+(\d{4})", text)
    if not m:
        return None
    mon = next((v for k, v in MONTHS.items() if k.startswith(m.group(2).lower()[:3])), None)
    if not mon:
        return None
    return datetime.date(int(m.group(3)), mon, int(m.group(1) or 1))


def _entries(path):
    items = []
    with open(path, encoding="utf-8") as fh:
        blocks = re.split(r"\n(?=- \*\*)", fh.read())
    for b in blocks:
        m = re.match(r"- \*\*(.+?)\*\*", b)
        if not m:
            continue
        dates = re.findall(r"\*([^*\n]+)\*\s*$", b.strip(), re.M)
        lines = [l.strip() for l in b.strip().splitlines()[1:] if l.strip() and not l.strip().startswith("*")]
        d = _date(dates[-1]) if dates else None
        items.append({"title": m.group(1), "where": lines[0] if lines else "", "when": dates[-1] if dates else "", "date": d})
    return items


def _workshops_latest(markdown, config):
    try:
        items = [e for e in _entries(os.path.join(config["docs_dir"], "talks", "workshops.md")) if e["date"]]
        items.sort(key=lambda e: e["date"], reverse=True)
        rows = "".join(
            f'<li><span class="bw-latest__tag">Workshop</span><strong>{e["title"]}</strong>'
            f'<span class="bw-latest__where">{e["where"]}</span><em>{e["when"]}</em></li>'
            for e in items[:4])
        return markdown.replace("<!-- workshops:latest -->", f'<ul class="bw-latest">{rows}</ul>')
    except Exception as exc:
        log.warning("workshops list skipped: %s", exc)
        return markdown


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri == "workshops/index.md":
        return _workshops_latest(markdown, config)
    if page.file.src_uri != "talks/index.md":
        return markdown
    try:
        base = os.path.join(config["docs_dir"], "talks")
        data = {name: _entries(os.path.join(base, name)) for name, _, _ in SOURCES}
        years = [e["date"].year for v in data.values() for e in v if e["date"]]
        stats = (
            '<div class="bw-stats">'
            f'<div><b>{len(data["talks.md"])}</b><span>Invited talks</span></div>'
            f'<div><b>{len(data["workshops.md"])}</b><span>Workshops</span></div>'
            f'<div><b>{len(data["tutorials.md"])}</b><span>Conference tutorials</span></div>'
            f'<div><b>{min(years)}</b><span>Speaking since</span></div>'
            '</div>')
        latest = sorted(((e, label) for name, label, _ in SOURCES for e in data[name] if e["date"]),
                        key=lambda x: x[0]["date"], reverse=True)[:4]
        rows = "".join(
            f'<li><span class="bw-latest__tag">{label}</span><strong>{e["title"]}</strong>'
            f'<span class="bw-latest__where">{e["where"]}</span><em>{e["when"]}</em></li>'
            for e, label in latest)
        markdown = markdown.replace("<!-- talks:stats -->", stats)
        markdown = markdown.replace("<!-- talks:latest -->", f'<ul class="bw-latest">{rows}</ul>')
        markdown = markdown.replace("<!-- talks:count:talks -->", str(len(data["talks.md"])))
        markdown = markdown.replace("<!-- talks:count:workshops -->", str(len(data["workshops.md"])))
        markdown = markdown.replace("<!-- talks:count:tutorials -->", str(len(data["tutorials.md"])))
    except Exception as exc:  # never break the site build over this page
        log.warning("talks hook skipped: %s", exc)
    return markdown
