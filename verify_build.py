"""Check generated local links/assets and directory/download consistency."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import csv, json

root = (Path(__file__).parent/'dist').resolve()
errors=[]
references=0
class Page(HTMLParser):
    def handle_starttag(self,tag,attrs):
        global references
        for key,value in attrs:
            if key not in ('href','src') or not value: continue
            url=urlsplit(value)
            if url.scheme or url.netloc: continue
            target = root/unquote(url.path).lstrip('/') if url.path.startswith('/') else self.file.parent/unquote(url.path)
            if not url.path: target=self.file
            if target.is_dir(): target=target/'index.html'
            references+=1
            if not target.exists(): errors.append(f'{self.file.relative_to(root)}: {value}')

files=list(root.rglob('*.html'))
for file in files:
    page=Page();page.file=file;page.feed(file.read_text(encoding='utf-8'))
records=json.loads((root.parent/'data/opportunities.json').read_text(encoding='utf-8'))
with (root/'downloads/opportunities.csv').open(encoding='utf-8-sig') as f: rows=list(csv.DictReader(f))
assert len(records)==len(rows)==30
assert (root/'opportunities/index.html').read_text(encoding='utf-8').count('class="opportunity"')==30
print(f'{len(files)} HTML pages; {references} local links/assets; {len(errors)} broken; 30 directory records match CSV.')
for error in errors: print(error)
raise SystemExit(bool(errors))
