"""Check generated local links/assets and the shared spreadsheet link."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote

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
home=(root/'index.html').read_text(encoding='utf-8')
assert 'https://docs.google.com/spreadsheets/d/1XfAbQf3lic7tOpiT_JgilAPFzAPPrtLPZBIZlM1TGBk/edit?usp=sharing' in home
assert not (root/'opportunities/index.html').exists()
print(f'{len(files)} HTML pages; {references} local links/assets; {len(errors)} broken; shared spreadsheet linked; old directory removed.')
for error in errors: print(error)
raise SystemExit(bool(errors))
