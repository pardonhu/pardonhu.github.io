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
            'author': 'Test <author>', 'category': {'en': 'Music & essays', 'zh': '音乐与随笔'},
            'date': '2026-09-28', 'summary': {'en': 'Test <script> & summary.', 'zh': '测试摘要。'}}]}

    def render(self, profile):
        (ROOT / ".local-audit").mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=ROOT / ".local-audit") as tmp:
            dest = Path(tmp)
            shutil.copytree(ROOT / 'templates', dest / 'templates')
            shutil.copytree(ROOT / 'assets/images', dest / 'assets/images')
            shutil.copytree(ROOT / 'assets/papers', dest / 'assets/papers')
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
        for term in ('Reading &amp; Essays', '读书与随笔', 'Abstract', '摘要', 'EM'):
            self.assertIn(term, page)
        for term in ('Author manuscript', '作者稿', 'Figure 2', '图 2', 'Spring 2024', '2024 年春季'):
            self.assertNotIn(term, page)
        self.assertNotIn('example.org', page)

    def test_four_actual_images(self):
        page = self.render(self.profile)[0].decode()
        self.assertIn('data-portrait src="'+self.profile['portrait']+'"', page)
        self.assertIn(self.profile['portrait_alt'], page)
        self.assertEqual(page.count('<figure class="pub-figure">'), 4)
        for pub in self.profile['publications']:
            card = build.render_publication(pub, self.profile['name'])
            self.assertTrue(pub.get('thumbnail'))
            if pub.get('thumbnail'):
                self.assertTrue((ROOT / pub['thumbnail']).is_file())
                if pub['id'] in ('prism', 'saga'):
                    self.assertEqual(pub['figure_number'], 2)
                    self.assertTrue(pub['figure_source'].endswith('#S2.F2'))
                else:
                    self.assertEqual(pub['figure_source'], 'User supplied; authorized by the site owner')
                self.assertIn(f'width="{pub["thumbnail_width"]}" height="{pub["thumbnail_height"]}"', card)
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

    def test_assigned_image_integrity(self):
        import hashlib
        from PIL import Image
        expected = {
            'fastset': ((788, 528), 'f73bdcf81eb97366a3fefdf0bd0676b65f81ed4388a8bd963780eb5f233f36f8'),
            'deepaoa': ((776, 348), 'b5f4ef432a82b78a45b94da73d4ac4c32df277e71c6998bab42d8e543c8fd681'),
        }
        for key, (size, digest) in expected.items():
            path = ROOT / f'assets/images/{key}-overview.jpg'
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), digest)
            with Image.open(path) as image:
                self.assertEqual(image.size, size)
                self.assertEqual(image.mode, 'RGB')
                self.assertFalse(image.getexif())
                # Only the minimal JFIF APP0 header is retained; no metadata APP segments or comments.
                self.assertTrue(all(marker == 'APP0' for marker, _ in image.applist))
                self.assertFalse(set(image.info) & {'exif', 'xmp', 'iptc', 'comment', 'photoshop'})
        css = (ROOT / 'assets/style.css').read_text()
        self.assertIn('width:100%;height:auto;object-fit:contain', css)

    def test_bio_and_education(self):
        p = self.profile
        self.assertEqual(p['education'][0]['period'], {'en':'2024–Present','zh':'2024–至今'})
        self.assertEqual(p['education'][0]['school'], {'en':'Global College','zh':'Global College'})
        self.assertEqual(p['education'][0]['advisor'], {'en':'Prof. Yibo Pi','zh':'皮宜博教授'})
        self.assertEqual(p['education'][1]['period'], {'en':'2021–2024','zh':'2021–2024 年'})
        self.assertEqual(p['education'][1]['advisor'], {'en':'Prof. Hongzi Zhu','zh':'朱弘恣教授'})
        self.assertEqual(p['education'][2], {
            'institution': {'en':'Shanghai Jiao Tong University','zh':'上海交通大学'},
            'degree': {'en':'Bachelor of Engineering','zh':'工学学士'},
            'period': {'en':'2013–2017','zh':'2013–2017 年'},
            'school': {'en': 'School of Mechanical Engineering and Power Engineering', 'zh': '机械与动力工程学院'},
            'major': {'en': 'Mechanical Engineering (Pilot Class)', 'zh': '机械工程（试点班）'}})
        self.assertEqual(p['education'][1]['institution'], p['education'][2]['institution'])
        page = self.render(p)[0].decode()
        for lang in ('en', 'zh'):
            self.assertIn(build.esc(p['bio'][lang]), page)
        for term in ('Graduate Student Member, IEEE', 'Bachelor of Engineering degree in 2017',
                     'master’s degree in 2024 from Shanghai Jiao Tong University', 'Prof. Hongzi Zhu',
                     '2017–2019', 'GAC Motor', 'automotive electronics and electrical systems',
                     'Global College', 'Prof. Yibo Pi', 'AI-enabled networking', 'wireless sensing'):
            self.assertIn(term, p['bio']['en'])
        for term in ('IEEE 研究生会员', '2017 年在上海交通大学获得工学学士学位',
                     '2024 年在上海交通大学获得硕士学位', '朱弘恣教授', '2017–2019 年在广汽乘用车',
                     '汽车电子电气相关工作', '皮宜博教授', '人工智能赋能的网络和无线感知'):
            self.assertIn(term, p['bio']['zh'])
        for stale in ('B.S.', '理学学士', '朱洪紫', '研究经历'):
            for content in (page, json.dumps(p, ensure_ascii=False),
                            (ROOT/'README_CN.md').read_text(), (ROOT/'SOURCES.md').read_text()):
                self.assertNotIn(stale, content)
        self.assertIn('"knowsAbout": ["AI-enabled networking", "Wireless sensing"]', page)

    def test_industry_experience_without_invented_fields(self):
        expected = [{'title': {'en':'GAC Motor','zh':'广汽乘用车'},
                     'detail': {'en':'Worked on automotive electronics and electrical systems','zh':'从事汽车电子电气相关工作'},
                     'period': {'en':'2017–2019','zh':'2017–2019 年'}}]
        self.assertEqual(self.profile['experience'], expected)
        page = self.render(self.profile)[0].decode()
        section = page.split('data-experience-index="0"', 1)[1].split('data-education-index=', 1)[0]
        for term in ('GAC Motor', '广汽乘用车', '2017–2019',
                     'Worked on automotive electronics and electrical systems', '从事汽车电子电气相关工作'):
            self.assertIn(term, section)
        for term in ('engineer', 'Engineer', 'Guangzhou', '广州', 'Shanghai', '上海', 'Research'):
            self.assertNotIn(term, section)

    def test_metadata_and_orcid(self):
        import re
        page = self.render(self.profile)[0].decode()
        orcid = 'https://orcid.org/0000-0003-0448-8907'
        self.assertEqual(self.profile['orcid'], orcid)
        self.assertEqual(page.count('href="'+orcid+'" target="_blank" rel="noopener noreferrer"'), 3)
        structured = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S)[1])
        self.assertIn(orcid, structured['sameAs'])
        self.assertEqual(structured['description'], self.profile['bio']['en'])
        for prefix in ('name="description"', 'property="og:description"'):
            self.assertIn(prefix+' content="'+build.esc(self.profile['bio']['en'])+'"', page)

    def test_prominent_orcid_and_confirmed_date_ranges(self):
        page = self.render(self.profile)[0].decode()
        feature = page.split('<p class="orcid-feature">', 1)[1].split('</p>', 1)[0]
        for text in ('ORCID profile', 'ORCID 研究者档案', '0000-0003-0448-8907'):
            self.assertIn(text, feature)
        self.assertIn('href="https://orcid.org/0000-0003-0448-8907"', feature)
        self.assertLess(page.index('class="orcid-feature"'), page.index('class="bio"'))
        section = page.split('id="background"', 1)[1].split('</section>', 1)[0]
        for period in ('2013–2017', '2017–2019', '2021–2024', '2024–Present', '2024–至今'):
            self.assertIn(period, section)
        self.assertNotIn('2019–2021', section)
        self.assertEqual(section.count('class="education-item background-item"'), 4)

    def test_baseline_preservation(self):
        import subprocess
        baseline = 'c2cc4ee2a2c98ae1635c649b61c62db9390d8af5'
        def old(path):
            return subprocess.check_output(['git','show',baseline+':'+path], cwd=ROOT)
        before = json.loads(old('profile.json'))
        next(p for p in before['publications'] if p['id']=='deepaoa')['paper_url'] = 'assets/papers/deepaoa-plus.pdf'
        next(p for p in before['publications'] if p['id']=='fastset')['paper_url'] = 'assets/papers/fastset.pdf'
        self.assertEqual(before, self.profile)
        self.assertTrue((ROOT/'assets/style.css').read_bytes().startswith(old('assets/style.css')))
        assets = subprocess.check_output(['git','ls-tree','-r','--name-only',baseline,'assets'], cwd=ROOT).decode().splitlines()
        for path in ['publications.bib'] + assets:
            self.assertEqual(old(path), (ROOT/path).read_bytes(), path)

    def test_only_internal_scope_removed_from_current_page(self):
        import subprocess
        import re
        baseline = subprocess.check_output(['git','show','c2cc4ee2a2c98ae1635c649b61c62db9390d8af5:index.html'], cwd=ROOT).decode()
        page = self.render(self.profile)[0].decode()
        for section in ('about','news','background','publications','reading-notes','contact'):
            pattern = r'<section[^>]* id="'+section+r'"[^>]*>.*?</section>'
            old_section = re.search(pattern, baseline, re.S)[0]
            current = re.search(pattern, page, re.S)[0]
            if section == 'publications':
                for path in ('assets/papers/deepaoa-plus.pdf','assets/papers/fastset.pdf'):
                    current = current.replace(build.anchor(path,'PDF'+build.icon('arrow'),'pub-link'), '')
            self.assertEqual(current, old_section, section)
        for text in ('owner-confirmed', 'not its entire archive', '经核验或由所有者确认', '尚无已核验', 'awaiting verification', '完整摘要待核验'):
            self.assertNotIn(text, page)
        missing = copy.deepcopy(self.profile['publications'][0])
        missing['abstract'] = None
        missing['abstract_evidence'] = {'status':'missing'}
        self.assertEqual(build.render_abstract(missing), '')
        missing['abstract_evidence'] = {}
        with self.assertRaises(ValueError):
            build.render_abstract(missing)

    def test_fastset_original_pdf(self):
        import hashlib
        raw = (ROOT/'assets/papers/fastset.pdf').read_bytes()
        self.assertEqual(len(raw), 13976470)
        self.assertEqual(hashlib.sha256(raw).hexdigest(), '8d62a7426e2bad98157b4c24d43e07e7112526c2785c1d3cc7b3836b173bd521')
        self.assertTrue(raw.startswith(b'%PDF-'))
        pub = next(p for p in self.profile['publications'] if p['id']=='fastset')
        card = build.render_publication(pub, self.profile['name'])
        self.assertIn('href="assets/papers/fastset.pdf" target="_blank" rel="noopener noreferrer"', card)
        self.assertIn('href="https://doi.org/10.1109/SECON68281.2026.11579146"', card)
        self.assertIn('href="https://ieeexplore.ieee.org/document/11579146/"', card)

    def test_deepaoa_pdf_and_safe_paths(self):
        import hashlib
        path = ROOT/'assets/papers/deepaoa-plus.pdf'
        raw = path.read_bytes()
        self.assertEqual(len(raw), 3588739)
        self.assertEqual(hashlib.sha256(raw).hexdigest(), 'c2fa56eccc8d529c30ed06d094254ac5bfd1f1f71a4c2b7a57b6f4ca878a01eb')
        self.assertTrue(raw.startswith(b'%PDF-'))
        pub = next(p for p in self.profile['publications'] if p['id']=='deepaoa')
        card = build.render_publication(pub, self.profile['name'])
        self.assertIn('href="assets/papers/deepaoa-plus.pdf" target="_blank" rel="noopener noreferrer"', card)
        self.assertIn('href="https://doi.org/10.1109/TVT.2024.3445722"', card)
        for value in ('../paper.pdf','/tmp/paper.pdf','assets/papers/../secret.pdf','assets/papers/%2e%2e/secret.pdf','//evil.test/a.pdf','javascript:alert(1)','file:///tmp/a.pdf','assets/papers/deepaoa-plus.pdf?x=1','assets/papers/missing.pdf'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                build.paper_pdf_url(value)

    def test_research_journey_exact_content_and_link(self):
        expected = {'url': 'https://github.com/pardonhu/facheng-research-journey', 'title': {'zh': '发成的科研探索之旅', 'en': 'Facheng’s Research Journey'}, 'description': {'zh': '记录我的科研探索：逐步形成自己的科研习惯与判断标准，学习如何评价一项工作、准备组会、寻找问题和设计实验，也保存尚未成熟的想法与值得反复阅读的论文。这不是一份完成的方法论，而是一份由我持续书写、修正和积累的研究笔记。', 'en': 'A record of my research explorations: gradually developing my own research habits and criteria for judgment, learning how to evaluate a piece of work, prepare for group meetings, identify research questions, and design experiments, while also keeping ideas that are still taking shape and papers worth revisiting. This is not a finished methodology, but a collection of research notes that I continue to write, revise, and build upon.'}}
        self.assertEqual(self.profile['research_journey'], expected)
        page = self.render(self.profile)[0].decode()
        for field in ('title','description'):
            for lang in ('en','zh'):
                self.assertIn(build.esc(expected[field][lang]), page)
        self.assertIn('href="'+expected['url']+'" target="_blank" rel="noopener noreferrer"', page)
        self.assertEqual(page.count('href="#research-journey"'), 2)
        self.assertLess(page.index('id="publications"'),page.index('id="research-journey"'))
        self.assertLess(page.index('id="research-journey"'),page.index('id="reading-notes"'))

    def test_majors_and_static_star_accent(self):
        page = self.render(self.profile)[0].decode()
        for entry in self.profile['education']:
            for lang in ('en', 'zh'):
                self.assertIn(build.esc(entry['major'][lang]), page)
        self.assertEqual(self.profile['education'][1]['school'], {'en':'Shanghai, China','zh':'中国上海'})
        for entry in self.profile['education']:
            self.assertNotIn('major_code', entry)
            self.assertNotIn('department', entry)
        self.assertIn('<div class="starfield" aria-hidden="true">', page)
        self.assertIn('focusable="false"', page)
        self.assertLess(page.index('class="starfield"'), page.index('<header'))
        css = (ROOT/'assets/style.css').read_text()
        self.assertIn('pointer-events:none', css)
        self.assertIn('@media(prefers-reduced-motion:reduce){.starfield', css)
        self.assertNotIn('@keyframes', css)

    def test_background_order_and_labels(self):
        page = self.render(self.profile)[0].decode()
        section = page.split('id="background"', 1)[1].split('</section>', 1)[0]
        markers = ['data-education-index="2"', 'data-experience-index="0"',
                   'data-education-index="1"', 'data-education-index="0"']
        self.assertEqual(section.count('class="education-item background-item"'), 4)
        positions = [section.index(marker) for marker in markers]
        self.assertEqual(positions, sorted(positions))
        self.assertIn('Master’s degree', section)
        self.assertNotIn('master’s degree', section)
        self.assertIn(build.bi('Background', '个人履历'), section)
        self.assertEqual(page.count('href="#background"'), 2)
        self.assertEqual(page.count(build.bi('Background', '个人履历')), 3)
        for stale in ('id="education"', 'id="experience"', 'href="#education"', 'href="#experience"', 'Selected Publications', '代表性论文'):
            self.assertNotIn(stale, page)
        self.assertIn('<h2 id="publications-heading">'+build.bi('Publications', '论文')+'</h2>', page)

    def test_author_optional_but_validated_when_present(self):
        notes = copy.deepcopy(self.notes)
        del notes['articles'][0]['author']
        build.validate_reading_notes(notes)
        page = build.render_reading_notes(notes)
        self.assertNotIn('reading-author', page)
        self.assertIn('Test &lt;title&gt;', page)
        for value in (None, '', ' ', 1, {}, []):
            notes['articles'][0]['author'] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                build.validate_reading_notes(notes)

    def test_qr_lossless_pixels_and_geometry(self):
        import hashlib
        from PIL import Image
        path = self.profile['reading_notes']['qr_image']
        self.assertEqual(path, 'assets/images/wechat-qr.png')
        self.assertEqual(hashlib.sha256((ROOT/path).read_bytes()).hexdigest(),
                         'd4942962acdf2914f66cebc59322c7addab6e81a19692be5998a017dd6a752b6')
        raw = (ROOT/path).read_bytes()
        offset = 8
        chunks = []
        while offset < len(raw):
            size = int.from_bytes(raw[offset:offset+4], 'big')
            chunks.append(raw[offset+4:offset+8])
            offset += size + 12
        self.assertEqual(offset, len(raw))
        self.assertEqual(chunks[0], b'IHDR')
        self.assertEqual(chunks[-1], b'IEND')
        self.assertTrue(set(chunks) <= {b'IHDR', b'IDAT', b'IEND'})
        with Image.open(ROOT/path) as im:
            self.assertEqual(im.size, (430,430))
            self.assertEqual(im.mode, 'RGB')
            self.assertEqual(hashlib.sha256(im.tobytes()).hexdigest(),
                             '3e20feffd5979df6b0c4af35f77167d5ba7be7b2b70b90ef972a2ec834f4f9a3')
            self.assertFalse(im.getexif())
            self.assertEqual(im.format, 'PNG')
            self.assertFalse(im.info)
            self.assertFalse(set(im.info) & {'exif','xmp','iptc','comment','photoshop','icc_profile'})
        page = build.render_reading_notes(self.profile['reading_notes'])
        self.assertIn('href="'+path+'"', page)
        self.assertIn('alt="杂记遣怀微信公众号二维码" width="430" height="430"', page)
        self.assertIn('Scan in WeChat', page)
        self.assertIn('微信扫码', page)
        css = (ROOT/'assets/style.css').read_text()
        self.assertIn('width:180px;height:180px;max-width:100%;object-fit:contain', css)
        for value in ('https://example.org/qr.jpg', '../qr.jpg', 'assets/images/portrait.jpg'):
            notes = copy.deepcopy(self.notes); notes['qr_image'] = value
            with self.assertRaises(ValueError):build.render_reading_notes(notes)

    def test_four_complete_actual_abstracts(self):
        self.assertEqual(len(self.profile["publications"]), 4)
        page = self.render(self.profile)[0].decode()
        self.assertEqual(page.count('<details class="abstract">'), 4)
        self.assertNotIn('class="abstract-missing"', page)
        for pub in self.profile['publications']:
            card = build.render_publication(pub, self.profile['name'])
            self.assertNotIn('description', pub)
            evidence = pub['abstract_evidence']
            self.assertEqual(evidence['title'], pub['title'])
            self.assertEqual(evidence['authors'], pub['authors'])
            self.assertIsInstance(pub['abstract'], dict)
            self.assertEqual(evidence['status'], 'verified')
            for lang in ('en', 'zh'):
                self.assertTrue(pub['abstract'][lang].strip())
                self.assertIn(build.esc(pub['abstract'][lang]), card)
            self.assertIn('<details class="abstract"><summary>', card)
        pub = copy.deepcopy(self.profile['publications'][1])
        pub['abstract'] = {'en':'First paragraph.\n\nLast <paragraph>.','zh':'第一段。\n\n最后一段。'}
        card = build.render_abstract(pub)
        self.assertIn('First paragraph.\n\nLast &lt;paragraph&gt;.', card)
        self.assertIn('第一段。\n\n最后一段。', card)


    def test_deepaoa_independent_source_positions(self):
        # Supplied raw evidence is intentionally local; never compare profile to itself.
        raw = json.loads((ROOT / '.local-audit/deepaoa-openalex.json').read_text())
        pub = next(p for p in self.profile['publications'] if p['id'] == 'deepaoa')
        self.assertEqual(raw['title'], pub['title'])
        self.assertEqual(raw['doi'].removeprefix('https://doi.org/').casefold(), pub['doi'].casefold())
        self.assertEqual([a['author']['display_name'] for a in raw['authorships']], pub['authors'])
        pairs = [(position, word) for word, positions in raw['abstract_inverted_index'].items()
                 for position in positions]
        self.assertTrue(all(type(i) is int and i >= 0 for i, _ in pairs))
        positions = [i for i, _ in pairs]
        self.assertEqual(len(positions), 239)
        self.assertEqual(len(set(positions)), len(positions), 'Duplicate source positions')
        self.assertEqual(sorted(positions), list(range(239)), 'Source position gaps')
        extracted = ' '.join(word for _, word in sorted(pairs))
        self.assertEqual(pub['abstract']['en'], extracted)
        displayed = pub['abstract']['en'].split(' ')
        for word, indexes in raw['abstract_inverted_index'].items():
            for index in indexes:
                self.assertEqual(displayed[index], word, f'Source position {index}')
        self.assertEqual(pub['abstract_evidence']['source'], 'https://api.openalex.org/works/https://doi.org/10.1109/TVT.2024.3445722')
        self.assertIn('third-party indexed abstract', pub['abstract_evidence']['version'])

    def test_fastset_independent_full_source_field(self):
        raw = json.loads((ROOT / '.local-audit/fastset-semanticscholar.json').read_text())
        pub = next(p for p in self.profile['publications'] if p['id'] == 'fastset')
        self.assertEqual(raw['title'], pub['title'])
        self.assertEqual(raw['externalIds']['DOI'], pub['doi'])
        # Check order independently, allowing only the documented second-name spelling.
        self.assertEqual([a['name'].replace('-', '').casefold() for a in raw['authors']],
                         [a.casefold() for a in pub['authors']])
        self.assertEqual(pub['authors'], ['Facheng Hu', 'Yunzhe Li', 'Hongzi Zhu', 'Xudong Wang'])
        markup = r'$\mathbf{5. 1}-\mathbf{5. 9} \times$'
        self.assertEqual(raw['abstract'].count(markup), 1)
        before, after = raw['abstract'].split(markup)
        self.assertEqual(pub['abstract']['en'], before + '5.1–5.9 ×' + after)
        self.assertEqual(pub['abstract']['en'].replace('5.1–5.9 ×', markup), raw['abstract'])
        self.assertEqual(pub['abstract_evidence']['source'],
                         'https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/SECON68281.2026.11579146?fields=title,authors,externalIds,abstract')
        self.assertIn('third-party indexed abstract', pub['abstract_evidence']['version'])

    def test_indexed_abstract_evidence_hashes_and_translation_claims(self):
        import hashlib
        for key, filename in [('fastset', 'fastset-semanticscholar.json'), ('deepaoa', 'deepaoa-openalex.json')]:
            pub = next(p for p in self.profile['publications'] if p['id'] == key)
            digest = hashlib.sha256((ROOT / '.local-audit' / filename).read_bytes()).hexdigest()
            self.assertEqual(pub['abstract_evidence']['source_sha256'], digest)
            self.assertIn('Complete Chinese translation', pub['abstract_evidence']['translation'])
        pubs = {p['id']:p for p in self.profile['publications']}
        for term in ('3GPP', 'TDL', 'OFDM', '5.1–5.9 倍', '3%', '基线', '冻结', '射线追踪'):
            self.assertIn(term, pubs['fastset']['abstract']['zh'])
        for term in ('四台同步', 'USRP', 'V2V', 'CSI', 'EM', '预训练', '错误分类', '最佳', '较低的延迟'):
            self.assertIn(term, pubs['deepaoa']['abstract']['zh'])

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
        self.assertNotIn('reading-empty', page)
        self.assertNotIn('尚无已核验', page)

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

    def test_optional_dates_categories_and_duplicates(self):
        n = copy.deepcopy(self.notes)
        del n['articles'][0]['date']
        build.validate_reading_notes(n)
        page = build.render_reading_notes(n)
        self.assertNotIn('<time', page)
        self.assertIn('Test &lt;author&gt;', page)
        self.assertIn('Music &amp; essays', page)
        self.assertIn('lang="zh-CN"', page)
        self.assertIn('Read in Chinese', page)
        self.assertIn('阅读原文', page)
        self.assertIn('rel="noopener noreferrer"', page)
        n['articles'].append(copy.deepcopy(n['articles'][0]))
        with self.assertRaises(ValueError): build.validate_reading_notes(n)
        for field in ('author', 'category'):
            for value in ('', None, {}, {'en': 'Only English'}, {'en': 'x', 'zh': ' '}):
                n = copy.deepcopy(self.notes); n['articles'][0][field] = value
                with self.subTest(field=field, value=value), self.assertRaises(ValueError):
                    build.validate_reading_notes(n)

    def test_verified_reading_originals(self):
        articles = self.profile['reading_notes']['articles']
        expected = [
            ('https://mp.weixin.qq.com/s/xrk3NmYKp0TA-j-8uzsUAA', '猎户星座', '发成'),
            ('https://mp.weixin.qq.com/s/wZiHg6oNw5ok62wXAi2_vA', '深宫修罗场——北魏子贵母死制度的黑色幽默', '何从'),
            ('https://mp.weixin.qq.com/s/xRUlN4Pcs_biWIcqLU_5BQ', '魏晋外貌协会大赏——侃《世说新语·容止》', '发成'),
            ('https://mp.weixin.qq.com/s/K9kZ77K7tmjc5PLO8gU52w', '“闻鸡起舞”少年们的升华人生', '发成'),
            ('https://mp.weixin.qq.com/s/cilRgAzcsfic_dd--5oJGw', '英雄迟暮《敕勒歌》', '发成'),
            ('https://mp.weixin.qq.com/s/qr12cl9yo03XHMPerka75g', '我怀念的 约翰 · 丹佛', None)]
        self.assertEqual(len(articles), 6)
        self.assertEqual([a['url'] for a in articles], [e[0] for e in expected])
        for link, title, author in expected:
            article = next(a for a in articles if a['url'] == link)
            self.assertEqual((article['title'], article.get('author')), (title, author))
            self.assertNotIn('date', article)  # No verified publication date yet.
        self.assertEqual(self.profile['reading_notes']['account_name'], '杂记遣怀')
        page = build.render_reading_notes(self.profile['reading_notes'])
        self.assertNotIn('reading-scope', page)
        self.assertNotIn('author', articles[-1])
        self.assertEqual(page.count('<img'), 1)
        self.assertEqual(page.count('class="reading-author"'), 5)
        self.assertNotIn('<iframe', page)

    def test_bad_dates(self):
        for value in ('2025-02-29', '2026-13-01', '20260928', '2026-9-28', '', None, 20260928):
            n = copy.deepcopy(self.notes);n['articles'][0]['date'] = value
            with self.subTest(value=value), self.assertRaises(ValueError):build.validate_reading_notes(n)

    def test_missing_and_overlong_fields(self):
        for field in ('url','title','category','summary'):
            n = copy.deepcopy(self.notes);del n['articles'][0][field]
            with self.subTest(field=field), self.assertRaises(ValueError):build.validate_reading_notes(n)
        for lang, value in (('en',''),('zh',''),('en','a'*321),('zh','字'*161),('en',None)):
            n = copy.deepcopy(self.notes);n['articles'][0]['summary'][lang] = value
            with self.subTest(lang=lang,value=value), self.assertRaises(ValueError):build.validate_reading_notes(n)
        for n in ({}, {'account_name':'','articles':[]}, {'account_name':'x','articles':None}):
            with self.assertRaises(ValueError):build.validate_reading_notes(n)

if __name__ == '__main__':unittest.main()
