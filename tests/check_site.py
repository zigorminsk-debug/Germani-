"""Basic checks for the static site and its HTML image map."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.areas = []
        self.images = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'area':
            self.areas.append(attrs)
        if tag == 'img':
            self.images.append(attrs)
        for name in ('href', 'src'):
            if name in attrs:
                self.links.append(attrs[name])


for name in ('index.html', 'berlin.html', 'dresden.html', 'frankfurt.html'):
    page = Page()
    page.feed((ROOT / name).read_text(encoding='utf-8'))
    for link in page.links:
        url = urlsplit(link)
        if not url.scheme and not url.netloc and url.path:
            assert (ROOT / url.path).is_file(), f'{name}: missing {link}'
    if name == 'index.html':
        assert any(image.get('usemap') == '#germany' for image in page.images)
        shapes = {area.get('href'): area.get('shape') for area in page.areas}
        assert shapes == {'berlin.html': 'circle', 'dresden.html': 'poly', 'frankfurt.html': 'poly'}, shapes
        for area in page.areas:
            assert area.get('alt') and area.get('coords') == area.get('data-coords')
    print(f'{name}: OK')
