import json
import csv
import re
from pathlib import Path
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
import xml.etree.ElementTree as ET

try:
    import yaml
except ModuleNotFoundError:
    yaml = None

REPO_DIR = Path(__file__).resolve()
while not ((REPO_DIR / 'data').exists() and (REPO_DIR / 'analysis').exists()):
    if REPO_DIR.parent == REPO_DIR:
        raise FileNotFoundError('Repository root not found')
    REPO_DIR = REPO_DIR.parent

NEWS_DIR = REPO_DIR / 'data/news'
PROJECT_DIR = REPO_DIR / 'analysis/headline_analysis'
ARCHIVE_DIR = PROJECT_DIR / 'archive'
PROJECT_DIR.mkdir(parents=True, exist_ok=True)
ARCHIVE_DIR.mkdir(exist_ok=True)


def save_json(obj, path: Path) -> None:
    """Write an object as JSON."""
    text = json.dumps(obj, indent=2, ensure_ascii=False)
    path.write_text(text + "\n", encoding='utf-8')


def archive_json(obj, archive_dir: Path, stem: str) -> None:
    """Save an archived JSON file."""
    archive_dir.mkdir(exist_ok=True)
    tag = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    save_json(obj, archive_dir / f'{stem}-{tag}.json')


def load_front_matter(path: Path) -> dict:
    """Return YAML front matter for a markdown file."""
    text = path.read_text(encoding='utf-8')
    match = re.search(r'^---\n(.*?)\n---', text, re.S)
    if not match:
        return {}
    front = match.group(1)
    if yaml:
        return yaml.safe_load(front)
    meta = {}
    for line in front.splitlines():
        if ':' in line:
            key, val = line.split(':', 1)
            meta[key.strip()] = val.strip()
    return meta


def collect_sources(news_dir: Path, out_dir: Path) -> list:
    """Collect news sources."""
    sources = []
    for index_path in news_dir.rglob('index.md'):
        meta = load_front_matter(index_path)
        title = meta.get('title')
        category = meta.get('category')
        src = meta.get('source')
        if title and category and src:
            sources.append({
                'title': str(title),
                'category': str(category),
                'source': str(src),
                'path': str(index_path.parent)
            })
    save_json(sources, out_dir / 'sources.json')
    archive_json(sources, out_dir / 'archive', 'sources')
    return sources


def parse_pubdate(date_str: str) -> datetime | None:
    """Parse a date string into UTC."""
    try:
        dt = parsedate_to_datetime(date_str) if date_str else None
        if dt is None:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def format_pubdate(dt: datetime | None) -> str:
    """Format a datetime for output."""
    return dt.strftime('%Y-%m-%d-%H-%M-%S +0000') if dt else ''


def parse_json_feed(path: Path) -> list:
    """Parse a JSON feed file."""
    items = []
    data = json.loads(path.read_text(encoding='utf-8'))
    for item in data.get('entries', []):
        title = item.get('title')
        link = item.get('link')
        pub = parse_pubdate(item.get('published'))
        if title and link:
            items.append({'title': title.strip(), 'link': link.strip(), 'pubdate': pub})
    return items


def parse_xml_feed(path: Path) -> list:
    """Parse an XML feed file."""
    items = []
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError:
        return items
    for item in root.iter():
        if item.tag.lower().endswith(('item', 'entry')):
            title = None
            link = None
            pub = None
            for child in item:
                tag = child.tag.lower()
                if tag.endswith('title'):
                    title = (child.text or '').strip()
                if tag.endswith('link'):
                    link = (child.text or '').strip() or child.attrib.get('href')
                if tag.endswith(('pubdate', 'published', 'updated')):
                    pub = parse_pubdate((child.text or '').strip())
            if title and link:
                items.append({'title': title, 'link': link, 'pubdate': pub})
    return items


def parse_feed(path: Path) -> list:
    """Parse a feed file of any supported type."""
    return parse_json_feed(path) if path.suffix == '.json' else parse_xml_feed(path)


def collect_headlines(sources: list, out_dir: Path) -> list:
    """Collect headlines from all sources."""
    headlines = []
    for src in sources:
        dir_path = Path(src['path'])
        latest = None
        for ext in ('.json', '.rss', '.xml'):
            fp = dir_path / f'latest{ext}'
            if fp.exists():
                latest = fp
                break
        if not latest:
            continue
        for item in parse_feed(latest):
            headlines.append({
                'headline': item['title'],
                'link': item['link'],
                'source': src['source'],
                'pubdate': item['pubdate']
            })
    min_time = datetime.min.replace(tzinfo=timezone.utc)
    headlines.sort(key=lambda r: r['pubdate'] or min_time, reverse=True)
    serial = [{**h, 'pubdate': format_pubdate(h['pubdate'])} for h in headlines]
    save_json(serial, out_dir / 'headlines.json')
    archive_json(serial, out_dir / 'archive', 'headlines')
    return headlines


def filter_headlines(headlines: list, delta: timedelta, name: str, out_dir: Path) -> list:
    """Filter headlines newer than cutoff."""
    cutoff = datetime.now(timezone.utc) - delta
    subset = [h for h in headlines if h['pubdate'] and h['pubdate'] >= cutoff]
    serial = [{**h, 'pubdate': format_pubdate(h['pubdate'])} for h in subset]
    save_json(serial, out_dir / f'{name}.json')
    archive_json(serial, out_dir / 'archive', name)
    return subset


def archive_csv(rows: list, archive_dir: Path, stem: str) -> None:
    """Archive a CSV file."""
    archive_dir.mkdir(exist_ok=True)
    tag = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    path = archive_dir / f'{stem}-{tag}.csv'
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['source', '1h', '24h', '7d'])
        writer.writeheader()
        writer.writerows(rows)


def build_summary(headlines: list, out_dir: Path) -> None:
    """Create summary counts for each source."""
    counts = {}
    now = datetime.now(timezone.utc)
    for h in headlines:
        src = h['source']
        dt = h['pubdate']
        if not dt:
            continue
        counts.setdefault(src, [0, 0, 0])
        if dt >= now - timedelta(hours=1):
            counts[src][0] += 1
        if dt >= now - timedelta(hours=24):
            counts[src][1] += 1
        if dt >= now - timedelta(days=7):
            counts[src][2] += 1
    rows = [{'source': s, '1h': c[0], '24h': c[1], '7d': c[2]} for s, c in counts.items()]
    rows.sort(key=lambda r: (-r['1h'], -r['24h'], -r['7d'], r['source']))
    out_path = out_dir / 'summary.csv'
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['source', '1h', '24h', '7d'])
        writer.writeheader()
        writer.writerows(rows)
    archive_csv(rows, out_dir / 'archive', 'summary')


def main() -> None:
    sources = collect_sources(NEWS_DIR, PROJECT_DIR)
    headlines = collect_headlines(sources, PROJECT_DIR)
    filter_headlines(headlines, timedelta(hours=1), '1h', PROJECT_DIR)
    filter_headlines(headlines, timedelta(hours=24), '24h', PROJECT_DIR)
    filter_headlines(headlines, timedelta(days=7), '7d', PROJECT_DIR)
    build_summary(headlines, PROJECT_DIR)


if __name__ == '__main__':
    main()
