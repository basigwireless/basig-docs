"""Fill in the Publications overview page at build time.

Counts the papers on publications/journal-publications.md and
publications/conference-publications.md (one "- **[Title](link)**" entry each)
and the books on publications/books-publications.md, and lists the newest papers.
"""
import os, re, logging

log = logging.getLogger("mkdocs.hooks.publications")
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


def _papers(path, kind):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    out = []
    for block in re.split(r"\n(?=- \*\*)", text):
        m = re.match(r"- \*\*(?:\[(.+?)\]\((\S+?)\)|(.+?))\*\*", block)
        if not m:
            continue
        lines = [l.strip() for l in block.strip().splitlines()]
        venue = lines[2] if len(lines) > 2 else ""
        years = re.findall(r"(?:19|20)\d{2}", venue)
        mon = next((i for i, mo in enumerate(MONTHS, 1) if re.search(r"\b" + mo, venue.lower())), 0)
        out.append({"title": m.group(1) or m.group(3), "url": m.group(2), "venue": venue,
                    "kind": kind, "key": (int(years[-1]) if years else 0, mon)})
    return out


def _split_date(venue, year):
    """Split '..., pp. 1-32, Sept. 2024' into ('..., pp. 1-32', 'Sept. 2024').
    If the venue has no separate date (e.g. '(ICETCI 2026)'), the date is just the year."""
    parts = [x.strip() for x in venue.rsplit(",", 1)]
    if len(parts) == 2 and re.search(r"(?:19|20)\d{2}", parts[1]) and not parts[1].endswith("*"):
        return parts[0], parts[1].rstrip(".")
    return venue, str(year) if year else ""


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "publications/index.md":
        return markdown
    try:
        base = os.path.join(config["docs_dir"], "publications")
        j = _papers(os.path.join(base, "journal-publications.md"), "Journal")
        c = _papers(os.path.join(base, "conference-publications.md"), "Conference")
        with open(os.path.join(base, "books-publications.md"), encoding="utf-8") as fh:
            books = len(re.findall(r'class="bw-book"', fh.read()))
        first = min(p["key"][0] for p in j + c if p["key"][0])
        stats = ('<div class="bw-stats">'
                 f'<div><b>{len(j)}</b><span>Journal articles</span></div>'
                 f'<div><b>{len(c)}</b><span>Conference papers</span></div>'
                 f'<div><b>{books}</b><span>Books</span></div>'
                 f'<div><b>{first}</b><span>Publishing since</span></div></div>')
        latest = sorted(j + c, key=lambda p: p["key"], reverse=True)[:4]
        rows = ""
        for p in latest:
            title = f'<a href="{p["url"]}" target="_blank" rel="noopener">{p["title"]}</a>' if p["url"] else p["title"]
            venue, when = _split_date(p["venue"], p["key"][0])
            venue = re.sub(r"\*(.+?)\*", r"<i>\1</i>", venue)
            rows += (f'<li><span class="bw-latest__tag">{p["kind"]}</span><strong>{title}</strong>'
                     f'<span class="bw-latest__where">{venue}</span><em>{when}</em></li>')
        markdown = markdown.replace("<!-- pubs:stats -->", stats)
        markdown = markdown.replace("<!-- pubs:latest -->", f'<ul class="bw-latest bw-latest--pubs">{rows}</ul>')
        markdown = markdown.replace("<!-- pubs:count:journal -->", str(len(j)))
        markdown = markdown.replace("<!-- pubs:count:conference -->", str(len(c)))
        markdown = markdown.replace("<!-- pubs:count:books -->", str(books))
    except Exception as exc:  # never break the site build over this page
        log.warning("publications hook skipped: %s", exc)
    return markdown
