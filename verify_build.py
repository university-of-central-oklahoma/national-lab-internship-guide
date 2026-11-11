"""Check generated local links/assets and both spreadsheet tab links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import yaml

root = (Path(__file__).parent/'dist').resolve()
config = yaml.safe_load((root.parent/'mkdocs.yml').read_text(encoding='utf-8'))
site_path = urlsplit(config.get('site_url', '')).path.rstrip('/')
errors=[]
references=0
class Page(HTMLParser):
    def handle_starttag(self,tag,attrs):
        global references
        for key,value in attrs:
            if key not in ('href','src') or not value: continue
            url=urlsplit(value)
            if url.scheme or url.netloc: continue
            local_path = unquote(url.path)
            if site_path and (local_path == site_path or local_path.startswith(site_path + '/')):
                local_path = local_path[len(site_path):] or '/'
            target = root/local_path.lstrip('/') if local_path.startswith('/') else self.file.parent/local_path
            if not url.path: target=self.file
            if target.is_dir(): target=target/'index.html'
            references+=1
            if not target.exists(): errors.append(f'{self.file.relative_to(root)}: {value}')

files=list(root.rglob('*.html'))
for file in files:
    page=Page();page.file=file;page.feed(file.read_text(encoding='utf-8'))
home=(root/'index.html').read_text(encoding='utf-8')
assert 'https://docs.google.com/spreadsheets/d/1XfAbQf3lic7tOpiT_JgilAPFzAPPrtLPZBIZlM1TGBk/edit?gid=0#gid=0' in home
assert 'https://docs.google.com/spreadsheets/d/1XfAbQf3lic7tOpiT_JgilAPFzAPPrtLPZBIZlM1TGBk/edit?gid=1254811916#gid=1254811916' in home
assert not (root/'opportunities/index.html').exists()
print(f'{len(files)} HTML pages; {references} local links/assets; {len(errors)} broken; DOE and Non-DOE spreadsheet tabs linked; old directory removed.')
for error in errors: print(error)
raise SystemExit(bool(errors))
