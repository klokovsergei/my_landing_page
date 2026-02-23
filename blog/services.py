import json
from pathlib import Path
import markdown

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / 'content' / 'articles'
INDEX_FILE = CONTENT_DIR / 'index.json'


def _load_index() -> list[dict]:
    if not INDEX_FILE.exists():
        return []
    with INDEX_FILE.open('r', encoding='utf-8') as f:
        return json.load(f)


def get_article_by_id(article_id: int) -> dict | None:
    items = _load_index()
    meta = next((x for x in items if x.get("id") == article_id), None)
    if not meta:
        return None

    md_path = CONTENT_DIR / meta["file"]
    if not md_path.exists():
        return None

    raw_md = md_path.read_text(encoding="utf-8")
    html = markdown.markdown(
        raw_md,
        extensions=["extra", "nl2br", "sane_lists"],
    )

    return {
        "id": meta["id"],
        "title": meta["title"],
        "description": meta.get("description", ""),
        "date": meta.get("date", ""),
        "read_time": meta.get("read_time", ""),
        "html": html,
    }
