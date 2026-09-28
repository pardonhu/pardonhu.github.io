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
        (ROOT / ".local-audit").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / ".local-audit") as tmp:
            dest = Path(tmp)
            shutil.copytree(ROOT / 'templates', dest / 'templates')
            shutil.copytree(ROOT / 'assets/images', dest / 'assets/images')
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
                if pub['abstract'] is not None:
                    self.assertTrue(pub['abstract'][lang])
        page = self.render(p)[0].decode()
        for term in ('Reading Notes', '读书笔记', 'Abstract', '摘要', 'EM'):
            self.assertIn(term, page)
        for term in ('Author manuscript', '作者稿', 'Figure 2', '图 2', 'Spring 2024', '2024 年春季'):
            self.assertNotIn(term, page)
        self.assertNotIn('example.org', page)

    def test_actual_images_and_text_only_cards(self):
        page = self.render(self.profile)[0].decode()
        self.assertIn('data-portrait src="'+self.profile['portrait']+'"', page)
        self.assertIn(self.profile['portrait_alt'], page)
        for pub in self.profile['publications']:
            card = build.render_publication(pub, self.profile['name'])
            if pub.get('thumbnail'):
                self.assertTrue((ROOT / pub['thumbnail']).is_file())
                self.assertEqual(pub['figure_number'], 2)
                self.assertTrue(pub['figure_source'].endswith('#S2.F2'))
                self.assertIn('href="'+pub['thumbnail']+'"', card)
                self.assertNotIn('href="'+pub['figure_source']+'"', card)
                for lang in ('en', 'zh'):
                    self.assertIn(pub['thumbnail_caption'][lang], card)
                self.assertIn(pub['thumbnail_alt'], card)
            else:
                self.assertIn('text-only', card)
                self.assertNotIn('<figure', card)
                self.assertNotIn('<img', card)
                self.assertNotIn('pub-cover', card)
        self.assertNotIn('prism-concept', page)

    def test_bio_and_education(self):
        p = self.profile
        expected = 'Facheng Hu (Graduate Student Member, IEEE) received the B.S. degree in 2017 and the master’s degree from Shanghai Jiao Tong University, Shanghai, China, in 2024, under the supervision of Prof. Hongzi Zhu. He is currently pursuing the Ph.D. degree at Global College, Shanghai Jiao Tong University, under the supervision of Prof. Yibo Pi. His research interests include AI-enabled networking and wireless sensing.'
        self.assertEqual(p['bio']['en'], expected)
        page = self.render(p)[0].decode()
        for lang in ('en', 'zh'):
            self.assertIn(build.esc(p['bio'][lang]), page)
        self.assertEqual(p['education'][0]['period'], {'en':'Present','zh':'在读'})
        self.assertEqual(p['education'][1]['period']['en'], '2024')
        self.assertEqual(p['education'][1]['advisor']['en'], 'Prof. Hongzi Zhu')
        self.assertNotIn('institution', p['education'][2])
        self.assertEqual(p['education'][2]['period']['en'], '2017')
        self.assertIn('"knowsAbout": ["AI-enabled networking", "Wireless sensing"]', page)

    def test_complete_abstract_rendering_and_missing_state(self):
        for pub in self.profile['publications']:
            card = build.render_publication(pub, self.profile['name'])
            self.assertNotIn('description', pub)
            evidence = pub['abstract_evidence']
            self.assertEqual(evidence['title'], pub['title'])
            self.assertEqual(evidence['authors'], pub['authors'])
            if pub['abstract'] is None:
                self.assertEqual(evidence['status'], 'missing')
                self.assertIn('Full abstract awaiting verification.', card)
                self.assertNotIn('<details class="abstract">', card)
            else:
                self.assertEqual(evidence['status'], 'verified')
                for lang in ('en', 'zh'):
                    self.assertIn(build.esc(pub['abstract'][lang]), card)
                self.assertIn('<details class="abstract"><summary>', card)
        pub = copy.deepcopy(self.profile['publications'][1])
        pub['abstract'] = {'en':'First paragraph.\n\nLast <paragraph>.','zh':'第一段。\n\n最后一段。'}
        card = build.render_abstract(pub)
        self.assertIn('First paragraph.\n\nLast &lt;paragraph&gt;.', card)
        self.assertIn('第一段。\n\n最后一段。', card)

    def test_abstract_evidence_and_translation_required(self):
        pub = copy.deepcopy(self.profile['publications'][1])
        for field in ('source', 'version', 'status'):
            broken = copy.deepcopy(pub)
            del broken['abstract_evidence'][field]
            with self.assertRaises(ValueError):build.render_abstract(broken)
        for lang in ('en', 'zh'):
            broken = copy.deepcopy(pub)
            broken['abstract'][lang] = ''
            with self.assertRaises(ValueError):build.render_abstract(broken)

    def test_fastset_citation(self):
        pub = next(p for p in self.profile['publications'] if p['id'] == 'fastset')
        self.assertEqual(pub['doi'], '10.1109/SECON68281.2026.11579146')
        self.assertEqual(pub['pages'], '150--158')
        self.assertEqual(pub['publication_record'], 'https://ieeexplore.ieee.org/document/11579146/')
        citation = build.bibtex(pub)
        self.assertIn('pages = {150--158}', citation)
        self.assertIn('doi = {'+pub['doi']+'}', citation)

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
