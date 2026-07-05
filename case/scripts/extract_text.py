from html.parser import HTMLParser
from pathlib import Path
import re

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []
        self.last_tag = ''
    def handle_starttag(self, tag, attrs):
        self.last_tag = tag
        if tag in {'script','style','svg','noscript'}:
            self.skip += 1
        if tag in {'p','div','section','article','main','h1','h2','h3','li','pre','tr','br'}:
            self.parts.append('\n')
        if tag in {'h1','h2','h3'}:
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in {'script','style','svg','noscript'} and self.skip:
            self.skip -= 1
        if tag in {'p','li','h1','h2','h3','pre','tr'}:
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip:
            s = data.strip()
            if s:
                self.parts.append(s + ' ')

def clean(text):
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    lines=[]
    seen_blank=False
    for line in text.splitlines():
        line=line.strip()
        if not line:
            if not seen_blank:
                lines.append('')
            seen_blank=True
        else:
            lines.append(line)
            seen_blank=False
    return '\n'.join(lines).strip()+"\n"

src=Path('case/sources/html')
out=Path('case/sources/text')
out.mkdir(parents=True, exist_ok=True)
for path in sorted(src.glob('*.html')):
    p=TextExtractor(); p.feed(path.read_text(encoding='utf-8', errors='ignore'))
    txt=clean(''.join(p.parts))
    (out/(path.stem+'.txt')).write_text(txt, encoding='utf-8')
    print(path.name, '->', path.stem+'.txt', len(txt))
