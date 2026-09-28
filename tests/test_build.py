"""Offline regression tests; synthetic fixtures render only in temporary test output, never production.
Test source itself may be published with the repository."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build

ROOT = Path(__file__).resolve().parents[1]

class BuildTests(unittest.TestCase):
    def setUp(self):
        self.profile = json.loads((ROOT / 'profile.json').read_text())
        self.notes = {'account_name': 'Test account', 'articles': [{
            'url': 'https://example.org/original', 'title': 'Test <title>',
            'date': '2026-09-28', 'summary': {'en': 'Test <script> & summary.', 'zh': '测试摘要。'}}]}

    def render(self, profile):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp)
            shutil.copytree(ROOT / 'templates', dest / 'templates')
            (dest / 'profile.json').write_text(json.dumps(profile))
            with patch.object(build, 'ROOT', dest):
                build.build()
            return tuple((dest / f).read_bytes() for f in ('index.html', 'publications.bib'))

    def test_determinism_and_checked_in_output(self):
        first = self.render(self.profile)
        self.assertEqual(first, self.render(self.profile))
        self.assertEqual(first, tuple((ROOT / f).read_bytes() for f in ('index.html', 'publications.bib')))

    def test_verified_source_fields(self):
        p = self.profile
        self.assertEqual(p['ieee_author_profile'], 'https://ieeexplore.ieee.org/author/996384661373839')
        prism = next(x for x in p['publications'] if x['id'] == 'prism')
        self.assertEqual(prism['authors'], ['Yunzhe Li','Facheng Hu','Hongzi Zhu','Quan Liu','Xiaoke Zhao','Jiangang Shen','Shan Chang','Minyi Guo'])
        self.assertEqual(prism['pages'], '1--10')
        self.assertEqual(prism['publication_record'], 'https://ieeexplore.ieee.org/document/11044768/')
        for pub in p['publications']:
            self.assertTrue(pub['source'].startswith('https://'))
            for lang in ('en', 'zh'):
                self.assertTrue(pub['description'][lang])
        page = self.render(p)[0].decode()
        for term in ('Reading Notes', '读书笔记', 'Original conceptual illustration', '非论文原图', 'NID', 'EM'):
            self.assertIn(term, page)
        self.assertNotIn('example.org', page)

    def test_empty_notes_render(self):
        profile = copy.deepcopy(self.profile)
        profile['reading_notes']['articles'] = []
        page = self.render(profile)[0].decode()
        self.assertNotIn('class="reading-note"', page)
        self.assertIn('reading-empty', page)
        self.assertIn('尚无已核验', page)

    def test_populated_render_and_escaping(self):
        self.profile['reading_notes'] = self.notes
        page = self.render(self.profile)[0].decode()
        self.assertIn('class="reading-note"', page)
        self.assertIn('Test &lt;title&gt;', page)
        self.assertIn('&lt;script&gt; &amp; summary.', page)
        self.assertIn('测试摘要。', page)
        self.assertIn('datetime="2026-09-28"', page)
        self.assertNotIn('reading-empty', page)

    def test_invalid_urls(self):
        for value in ('', 'http://example.org/a', '//example.org/a', 'javascript:alert(1)', 'https:///a', 'https://user:secret@example.org/a', 'https://example.org/a b', 'https://example.org/\\a', 'https://example.org:bad/a', 'https://example.org/a#fragment', 'https://bad..org/a', 'https://-bad.org/a'):
            with self.subTest(value=value):
                n = copy.deepcopy(self.notes);n['articles'][0]['url'] = value
                with self.assertRaises(ValueError):build.validate_reading_notes(n)

    def test_bad_dates(self):
        for value in ('2025-02-29', '2026-13-01', '20260928', '2026-9-28', ''):
            n = copy.deepcopy(self.notes);n['articles'][0]['date'] = value
            with self.subTest(value=value), self.assertRaises(ValueError):build.validate_reading_notes(n)

    def test_missing_and_overlong_fields(self):
        for field in ('url','title','date','summary'):
            n = copy.deepcopy(self.notes);del n['articles'][0][field]
            with self.subTest(field=field), self.assertRaises(ValueError):build.validate_reading_notes(n)
        for lang, value in (('en',''),('zh',''),('en','a'*321),('zh','字'*161),('en',None)):
            n = copy.deepcopy(self.notes);n['articles'][0]['summary'][lang] = value
            with self.subTest(lang=lang,value=value), self.assertRaises(ValueError):build.validate_reading_notes(n)
        for n in ({}, {'account_name':'','articles':[]}, {'account_name':'x','articles':None}):
            with self.assertRaises(ValueError):build.validate_reading_notes(n)

if __name__ == '__main__':unittest.main()
