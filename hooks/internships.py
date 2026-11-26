"""Fill in the Internships overview page at build time.

Counts interns, institutes and ongoing projects from internships/past-current.md,
internships/ugpgprojects.md and internships/visiting-scholars.md, so the numbers on
internships/index.md stay correct when those pages are updated.
"""
import os, re, logging

log = logging.getLogger("mkdocs.hooks.internships")


def _people(path):
    """Intern lines look like:  '    - Name <span class="bw-inst">Institute, City</span> *dates*'."""
    with open(path, encoding="utf-8") as fh:
        return re.findall(r'^\s+- (.+?) <span class="bw-inst">(.+?)</span>', fh.read(), re.M)


def _projects(path):
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and cells[0].isdigit():
                rows.append(cells)
    return rows


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "internships/index.md":
        return markdown
    try:
        base = os.path.join(config["docs_dir"], "internships")
        interns = _people(os.path.join(base, "past-current.md"))
        scholars = _people(os.path.join(base, "visiting-scholars.md"))
        projects = _projects(os.path.join(base, "ugpgprojects.md"))
        with open(os.path.join(base, "past-current.md"), encoding="utf-8") as fh:
            years = [int(y) for y in re.findall(r"^## (\d{4})", fh.read(), re.M)]
        inst = {i.split(",")[0].strip().lower() for _, i in interns + scholars}
        inst |= {r[2].split(",")[0].strip().lower() for r in projects}
        ongoing = sum(1 for r in projects if "Ongoing" in r[-1])
        stats = (
            '<div class="bw-stats">'
            f'<div><b>{len({n.strip().lower() for n, _ in interns})}</b><span>Interns mentored</span></div>'
            f'<div><b>{len(inst)}</b><span>Institutes</span></div>'
            f'<div><b>{ongoing}</b><span>Ongoing student projects</span></div>'
            f'<div><b>{min(years)}</b><span>Mentoring since</span></div>'
            '</div>')
        markdown = markdown.replace("<!-- interns:stats -->", stats)
        markdown = markdown.replace("<!-- interns:count:interns -->", str(len({n.strip().lower() for n, _ in interns})))
        markdown = markdown.replace("<!-- interns:count:projects -->", str(len(projects)))
        markdown = markdown.replace("<!-- interns:count:scholars -->", str(len(scholars)))
    except Exception as exc:  # never break the site build over this page
        log.warning("internships hook skipped: %s", exc)
    return markdown
