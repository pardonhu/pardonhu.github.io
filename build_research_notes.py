"""Render the featured Markdown reports from a local facheng-research-journey checkout.

Install Markdown 3.9 and run: python build_research_notes.py PATH_TO_NOTES
The generated pages, images and downloadable template are served as static files.
"""

import argparse
import html
import json
import re
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

import markdown

ROOT = Path(__file__).resolve().parent


def render(notes: Path) -> None:
    journey = json.loads((ROOT / 'profile.json').read_text(encoding='utf-8'))['research_journey']
    paths = { (notes / item['source']).resolve(): item['slug'] for item in journey['reports'] }
    for item in journey['reports']:
        source = notes / item['source']
        folder = ROOT / 'research-notes' / item['slug']
        folder.mkdir(parents=True, exist_ok=True)
        body = markdown.markdown(source.read_text(encoding='utf-8-sig'), extensions=['tables', 'fenced_code'])
        article = ET.fromstring('<article>' + body + '</article>')
        for link in article.iter('a'):
            parsed = urlsplit(link.attrib['href'])
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (source.parent / unquote(parsed.path)).resolve()
            dest = ('../' + paths[target] + '/') if target in paths else (
                journey['url'] + '/blob/main/' + quote(target.relative_to(notes).as_posix())
            )
            link.set('href', dest + ('#' + parsed.fragment if parsed.fragment else ''))
        for image in article.iter('img'):
            image_path = (source.parent / unquote(image.attrib['src'])).resolve()
            if not image_path.is_relative_to(notes):
                raise ValueError('Image outside the notes repository: ' + str(image_path))
            assets = folder / 'images'
            assets.mkdir(exist_ok=True)
            shutil.copyfile(image_path, assets / image_path.name)
            image.set('src', 'images/' + quote(image_path.name))
            image.set('loading', 'lazy')

        paragraphs = list(article)
        for paragraph, caption in zip(paragraphs, paragraphs[1:]):
            if paragraph.tag == 'p' and len(paragraph) == 1 and paragraph[0].tag == 'img' and (
                caption.tag == 'p' and re.match(r'图\d+[.．]', caption.text or '')
            ):
                paragraph.tag = 'figure'
                article.remove(caption)
                caption.tag = 'figcaption'
                paragraph.append(caption)

        title = html.escape(article.find('h1').text)
        navigation = '<a href="../../#research-journey">胡发成 · 科研笔记</a>'
        if item['slug'] == 'report-template':
            title = html.escape(item['title']['zh'])
            shutil.copyfile(source, folder / source.name)
            navigation += '<a href="' + quote(source.name) + '" download>下载空白模板（Markdown）</a>'
        page = f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · 胡发成的科研笔记</title>
  <link rel="stylesheet" href="../notes.css">
</head>
<body>
  <nav aria-label="科研笔记">{navigation}</nav>
  <main>{ET.tostring(article, encoding='unicode', method='html')}</main>
</body>
</html>
'''
        (folder / 'index.html').write_text(page, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('notes', type=Path)
    render(parser.parse_args().notes.resolve())
