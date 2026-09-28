#!/usr/bin/env python3
"""Build the static homepage from profile.json, with the Python standard library only.

Usage: python build.py
The generated index.html works without a server and has readable content without JS.
Only include information you intend to publish: all repository files may be public.
"""
from __future__ import annotations
from datetime import date
import html
import json
import re
import sys
from pathlib import Path
from string import Template
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent

def esc(value: object) -> str:
    return html.escape(str(value), quote=True)

def localize(value: object, lang: str) -> str:
    if isinstance(value, dict):
        return str(value.get(lang, value.get('en', '')))
    return str(value or '')

def bi(en: str, zh: str, *, raw: bool = False) -> str:
    a, b = (en, zh) if raw else (esc(en), esc(zh))
    return f'<span data-lang="en" lang="en">{a}</span><span data-lang="zh" lang="zh-CN">{b}</span>'

def localized(value: object) -> str:
    return bi(localize(value, 'en'), localize(value, 'zh'))

def url(value: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError('An enabled link has an empty URL.')
    parsed = urlparse(value)
    if parsed.scheme and parsed.scheme not in ('https', 'http', 'mailto'):
        raise ValueError(f'Unsupported URL scheme: {parsed.scheme}')
    if value.startswith('//') or '\\' in value:
        raise ValueError(f'Invalid URL: {value}')
    if not parsed.scheme and (value.startswith('/') or '..' in Path(value).parts):
        raise ValueError(f'Use a relative path inside the website: {value}')
    return esc(value)

def validate_reading_notes(notes: object) -> None:
    if not isinstance(notes, dict) or not isinstance(notes.get('account_name'), str) or not notes['account_name'].strip():
        raise ValueError('reading_notes requires account_name.')
    if not isinstance(notes.get('articles'), list):
        raise ValueError('reading_notes.articles must be a list.')
    seen = set()
    for entry in notes['articles']:
        if not isinstance(entry, dict):
            raise ValueError('Each reading note must be an object.')
        for field in ('url', 'title', 'date'):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                raise ValueError('Reading note requires ' + field)
        link = entry['url']
        parsed = urlparse(link)
        if (parsed.scheme != 'https' or not parsed.hostname or '.' not in parsed.hostname
                or parsed.username or parsed.password or parsed.fragment or parsed.hostname.endswith('.')
                or any(c.isspace() or ord(c) < 32 for c in link) or '\\' in link):
            raise ValueError('Reading notes require original absolute HTTPS URLs without credentials or fragments.')
        hostname = parsed.hostname.encode('idna').decode('ascii')
        if len(hostname) > 253 or any(not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?', part) for part in hostname.split('.')):
            raise ValueError('Invalid reading note hostname.')
        try:
            parsed.port
        except ValueError as exc:
            raise ValueError('Invalid reading note URL port.') from exc
        if link in seen:
            raise ValueError('Duplicate reading note URL.')
        seen.add(link)
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', entry['date']):
            raise ValueError('Reading note date must be YYYY-MM-DD.')
        date.fromisoformat(entry['date'])
        summary = entry.get('summary')
        for lang, limit in (('en', 320), ('zh', 160)):
            if not isinstance(summary, dict) or not isinstance(summary.get(lang), str) or not summary[lang].strip() or len(summary[lang]) > limit:
                raise ValueError(f'Reading note requires a short {lang} summary (max {limit} characters).')

def render_reading_notes(notes: dict) -> str:
    validate_reading_notes(notes)
    account = bi('Public account: ', '公众号：') + esc(notes['account_name'])
    entries = []
    for entry in notes['articles']:
        entries.append('<article class="reading-note"><h3>' + anchor(entry['url'], esc(entry['title']))
                       + '</h3><time datetime="' + esc(entry['date']) + '">' + esc(entry['date'])
                       + '</time><p>' + localized(entry['summary']) + '</p></article>')
    body = ''.join(entries) if entries else '<p class="reading-empty">' + bi(
        'No public article links have been verified yet. Original links will be curated here.',
        '尚无已核验的公开文章链接；这里将整理文章原始链接。') + '</p>'
    return '<section class="reading-notes section-card card" id="reading-notes" aria-labelledby="reading-heading"><h2 id="reading-heading">' + bi('Reading Notes', '读书笔记') + '</h2><p class="reading-account">' + account + '</p>' + body + '</section>'

ICONS = {
    'mail':'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
    'copy':'<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V4H4v12h4"/>',
    'arrow':'<path d="M7 17 17 7M7 7h10v10"/>',
    'school':'<path d="m2 8 10-5 10 5-10 5L2 8Zm4 3v6c4 3 8 3 12 0v-6M22 8v8"/>',
    'person':'<circle cx="12" cy="7" r="3"/><path d="M5 21v-3a7 7 0 0 1 14 0v3"/>',
    'link':'<path d="m10 13 4-4M8 15l-2 2a4 4 0 0 1-5-5l5-5a4 4 0 0 1 6 0m0 2 3-3a4 4 0 0 1 5 5l-5 5a4 4 0 0 1-6 0"/>',
    'code':'<path d="m8 5-6 7 6 7m8-14 6 7-6 7m-5 0 2-14"/>',
    'file':'<path d="M14 2H5v20h14V7l-5-5Zm0 0v5h5M8 12h8m-8 4h8"/>',
}

def icon(name: str) -> str:
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+ICONS[name]+'</svg>'

def anchor(href: str, text: str, cls: str = '', icon_name: str = '', external: bool = True) -> str:
    attrs = ' target="_blank" rel="noopener noreferrer"' if external and not href.startswith('mailto:') else ''
    return f'<a class="{esc(cls)}" href="{url(href)}"{attrs}>'+(icon(icon_name) if icon_name else '')+text+'</a>'

def bibtex(p: dict) -> str:
    def b(value: object) -> str:
        return str(value).replace('&', r'\&')
    authors = ' and '.join(p['authors'])
    venue_key = 'journal' if p['type'] == 'article' else 'booktitle'
    fields = [('title', '{'+p['title']+'}'), ('author', authors), (venue_key, p['venue']), ('year', str(p['year']))]
    for key in ('volume','number','pages','doi'):
        if p.get(key): fields.append((key, p[key]))
    return '@'+p['type']+'{'+p['bibkey']+',\n'+',\n'.join(f'  {k} = {{{b(v)}}}' for k,v in fields)+'\n}'

def render_publication(p: dict, name: str) -> str:
    paper_link = 'https://doi.org/'+p['doi'] if p.get('doi') else p.get('paper_url') or p.get('source')
    if not paper_link:
        raise ValueError(f'Publication {p.get("id")} has no source or paper URL.')
    author_html=[]
    for a in p['authors']:
        text='<strong>'+esc(a)+'</strong>' if a == name else esc(a)
        if a in p.get('equal_contributors',[]): text += '<sup>*</sup>'
        author_html.append(text)
    if p.get('thumbnail'):
        image = ('<img loading="lazy" src="'+url(p['thumbnail'])+'" alt="'
                 +esc(p['thumbnail_alt'])+'" width="'+esc(p['thumbnail_width'])
                 +'" height="'+esc(p['thumbnail_height'])+'">')
        source = anchor(p['figure_source'], bi('Author manuscript · Figure '+str(p['figure_number']),
                        '作者稿 · 图 '+str(p['figure_number'])), 'figure-source')
        cover = ('<figure class="pub-figure">'+anchor(p['thumbnail'], image, 'figure-image')
                 +'<figcaption>'+localized(p['thumbnail_caption'])+' '+source
                 +'</figcaption></figure>')
    else:
        cover = ''
    buttons = []
    if p.get("publication_record"): buttons.append(anchor(p["publication_record"], bi("IEEE publication record", "IEEE 发表记录")+icon("arrow"), "pub-link"))
    if p.get('doi'): buttons.append(anchor('https://doi.org/'+p['doi'],bi('Publisher','出版页面')+icon('arrow'),'pub-link'))
    if p.get('arxiv'):
        buttons.append(anchor('https://arxiv.org/abs/'+p['arxiv'],'arXiv'+icon('arrow'),'pub-link'))
        buttons.append(anchor('https://arxiv.org/pdf/'+p['arxiv'],'PDF'+icon('arrow'),'pub-link'))
    elif p.get('paper_url'):
        buttons.append(anchor(p['paper_url'],'PDF'+icon('arrow'),'pub-link'))
    if not any(p.get(k) for k in ('doi', 'arxiv', 'paper_url')) and p.get('source'):
        label = p.get('source_label', {'en': 'Publication record', 'zh': '发表记录'})
        buttons.append(anchor(p['source'], localized(label)+icon('arrow'), 'pub-link'))
    for key,en,zh in [('code_url','Code','代码'),('project_url','Project','项目')]:
        if p.get(key): buttons.append(anchor(p[key],bi(en,zh)+icon('arrow'),'pub-link'))
    venue = esc(p['venue'])
    if p.get('volume'):
        venue += ', '+esc(p['volume'])+'('+esc(p.get('number',''))+')'
    if p.get('pages'): venue += ', pp. '+esc(p['pages'].replace('--','–'))
    venue += ', '+esc(p['year'])+'.'
    codeid = 'bib-'+p['id']
    return f'''<article class="publication-card card{' has-figure' if cover else ' text-only'}" data-year="{esc(p['year'])}" id="paper-{esc(p['id'])}">
      {cover}<div class="pub-content">
        <div class="pub-meta">{esc(p['venue_short'])} {esc(p['year'])}</div>
        <h3 class="pub-title">{anchor(paper_link,esc(p['title']))}</h3>
        <p class="pub-authors">{', '.join(author_html)}</p>
        <p class="pub-venue">{venue}</p>
        <p class="pub-description">{localized(p.get('description',''))}</p>
        <div class="pub-links">{''.join(buttons)}</div>
        <details class="citation">
          <summary class="cite-toggle">{bi('Cite / BibTeX','引用 / BibTeX')}</summary>
          <div class="citation-box"><pre><code id="{codeid}">{esc(bibtex(p))}</code></pre>
          <button class="copy-citation js-only" type="button" data-copy-citation="{codeid}">{icon('copy')}{bi('Copy BibTeX','复制 BibTeX')}</button></div>
        </details>
      </div>
    </article>'''

def optional_section(items: list, section_id: str, en: str, zh: str) -> str:
    if not items: return ''
    rendered=[]
    for item in items:
        rendered.append('<div class="optional-item"><strong>'+localized(item['title'])+'</strong><br><small>'+localized(item.get('detail',''))+' · '+localized(item.get('period',''))+'</small></div>')
    return f'<section class="optional-section card" id="{section_id}"><h2>{bi(en,zh)}</h2>'+''.join(rendered)+'</section>'

def build() -> None:
    p = json.loads((ROOT/'profile.json').read_text(encoding='utf-8'))
    required=('name','name_zh','role','institution','school','advisor','email','publications','education')
    missing=[k for k in required if k not in p]
    if missing: raise ValueError('Missing profile fields: '+', '.join(missing))
    if not isinstance(p['publications'],list): raise ValueError('publications must be a list.')
    if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', p['email']): raise ValueError('Invalid contact email.')
    username=p.get('github_username','').strip()
    if username and not re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?',username):
        raise ValueError('github_username must be a username, not a URL or a credential.')
    ids=[x['id'] for x in p['publications']]
    if len(ids)!=len(set(ids)) or any(not re.fullmatch(r'[a-z0-9-]+',x) for x in ids):
        raise ValueError('Each publication id must be unique and use lowercase letters, digits or hyphens.')
    email_link='mailto:'+p['email']
    institution=anchor(p['institution_url'],localized(p['institution']))
    school=anchor(p['school_url'],localized(p['school']))
    advisor=anchor(p['advisor']['url'],bi('Prof. '+p['advisor']['name'],p['advisor']['name_zh']+'老师'))
    bio_en=f'I am a Ph.D. student at {anchor(p["school_url"],esc(localize(p["school"],"en")))}, {anchor(p["institution_url"],esc(localize(p["institution"],"en")))}, advised by {anchor(p["advisor"]["url"],esc("Prof. "+p["advisor"]["name"]))}.'
    bio_zh=f'我是{anchor(p["institution_url"],esc(localize(p["institution"],"zh")))} {anchor(p["school_url"],esc(localize(p["school"],"zh")))} 的博士研究生，导师是{anchor(p["advisor"]["url"],esc(p["advisor"]["name_zh"]+"老师"))}。'
    if p.get('portrait'):
        path=ROOT/p['portrait']
        if not path.is_file(): raise ValueError(f'Portrait file is missing: {p["portrait"]}')
        portrait=f'<div class="portrait has-photo" data-initials="{esc(p["initials"])}"><img data-portrait src="{url(p["portrait"])}" alt="{esc(p.get("portrait_alt", p["name"]))}" width="150" height="150"></div>'
    else:
        portrait=f'<div class="portrait" aria-label="{esc(p["name"])} initials"><span class="monogram">{esc(p["initials"])}</span></div>'
    contact_links=[anchor(email_link,icon('mail')+esc(p['email']),'contact-link',external=False),
                   f'<button type="button" class="copy-email js-only" data-copy="{esc(p["email"])}" aria-label="Copy email address">{icon("copy")}</button>']
    side_links=[anchor(email_link,bi('Email','电子邮件'),'','mail',False)]
    socials=[]
    if username: socials.append(('https://github.com/'+username,'GitHub','GitHub','code'))
    if p.get('ieee_author_profile'):socials.append((p['ieee_author_profile'],'IEEE author profile','IEEE 作者主页','person'))
    if p.get('google_scholar'):socials.append((p['google_scholar'],'Google Scholar','Google 学术','school'))
    if p.get('orcid'):socials.append((p['orcid'],'ORCID','ORCID','link'))
    if p.get('cv_url'):socials.append((p['cv_url'],'Curriculum Vitae','个人简历','file'))
    for href,en,zh,ico in socials:
        contact_links.append('<span class="contact-separator" aria-hidden="true"></span>'+anchor(href,icon(ico)+bi(en,zh),'contact-link'))
        side_links.append(anchor(href,bi(en,zh),'',ico))
    if not socials:
        contact_links.append('<span class="contact-separator" aria-hidden="true"></span>'+anchor(p['advisor']['url'],icon('person')+bi("Advisor","导师主页"),'contact-link'))
    side_links.extend([anchor(p['institution_url'],bi('University','学校主页'),'','school'),anchor(p['advisor']['url'],bi('Advisor','导师主页'),'','person')])
    news=''.join(f'<li class="news-item"><span class="news-date">{esc(n["date"])}</span><div>{anchor(n["url"],localized(n["text"])) if n.get("url") else localized(n["text"])}</div></li>' for n in p.get('news',[]))
    education=''.join(f'''<div class="education-item"><div class="education-icon" aria-hidden="true">{icon('school')}</div><div><div class="education-name">{localized(e['institution'])}</div><div class="education-school">{localized(e.get('school',''))}</div><div class="education-degree">{localized(e['degree'])}</div><div class="education-period">{localized(e['period'])}</div></div></div>''' for e in p['education'])
    pubs=sorted(p['publications'],key=lambda x:-int(x['year']))
    years=sorted({int(x['year']) for x in pubs},reverse=True)
    filters='<button type="button" class="filter" data-filter="all" aria-pressed="true">'+bi('All','全部')+'</button>'+''.join(f'<button type="button" class="filter" data-filter="{y}" aria-pressed="false">{y}</button>' for y in years)
    interests=''
    if p.get('research_interests'):
        interests='<div class="interests">'+''.join('<span class="interest">'+localized(x)+'</span>' for x in p['research_interests'])+'</div>'
    extra=''
    if localize(p.get('extra_bio',''),'en') or localize(p.get('extra_bio',''),'zh'):extra='<div class="extra-bio">'+localized(p['extra_bio'])+'</div>'
    updated=str(p.get('updated',''))
    updated_en=updated_zh=updated
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}',updated):
        import datetime
        date=datetime.date.fromisoformat(updated)
        updated_en=date.strftime('%b %Y');updated_zh=f'{date.year} 年 {date.month} 月'
    description=f'{p["name"]} ({p["name_zh"]}), Ph.D. student at Shanghai Jiao Tong University. Biography, selected publications, and contact information.'
    structured={"@context":"https://schema.org","@type":"Person","name":p['name'],"alternateName":p['name_zh'],"jobTitle":localize(p['role'],'en'),"affiliation":{"@type":"CollegeOrUniversity","name":localize(p['institution'],'en')},"email":email_link}
    sameas=[x[0] for x in socials if x[1] != 'Curriculum Vitae']
    if sameas:structured['sameAs']=sameas
    website_url=p.get('website_url','').strip() or ('https://'+username.lower()+'.github.io/' if username else '')
    canonical=''
    if website_url:
        canonical='<link rel="canonical" href="'+url(website_url)+'">\n<meta property="og:url" content="'+url(website_url)+'">'
        structured['url']=website_url
    rendered=Template((ROOT/'templates/page.html').read_text(encoding='utf-8')).substitute(
        lang='zh-CN' if p.get('default_language')=='zh' else 'en', name=esc(p['name']), initials=esc(p['initials']), name_zh=esc(p['name_zh']),
        meta_description=esc(description),canonical=canonical,structured=json.dumps(structured,ensure_ascii=False).replace('<','\\u003c'),
        nav_reading=bi('Reading Notes','读书笔记'),reading_notes=render_reading_notes(p['reading_notes']),
        nav_about=bi('About','简介'),nav_pubs=bi('Publications','论文'),nav_education=bi('Education','教育'),nav_contact=bi('Contact','联系'),
        sidebar_heading=bi('On this page','页面导航'),connect=bi('Connect','学术联系'),side_links=''.join(side_links),
        role=localized(p['role']),institution=institution,school=school,advisor=advisor,advised_by=bi('Advised by','导师'),portrait=portrait,
        bio=bi(bio_en,bio_zh,raw=True),extra_bio=extra,interests=interests,contact_links=''.join(contact_links),
        news_label=bi('News','动态'),news=news,education_label=bi('Education','教育经历'),education=education,
        publications_label=bi('Selected Publications','代表性论文'),contribution_note=bi('* Equal contribution.','* 表示共同贡献。'),filters=filters,
        publication_cards=''.join(render_publication(x,p['name']) for x in pubs),
        optional_sections=optional_section(p.get('experience',[]),'experience','Experience','研究经历')+optional_section(p.get('awards',[]),'awards','Honors & Awards','荣誉与奖励'),
        contact_caption=bi('The best way to reach me is by email.','欢迎通过电子邮件联系。'),contact_button=anchor(email_link,icon('mail')+esc(p['email']),'contact-button',external=False),
        copyright=esc(updated[:4] if updated else '2026'),updated=bi('Updated '+updated_en,updated_zh+'更新'),
        footer_credit=bi('Layout inspired by','布局参考')+' '+anchor('https://haifengjia.github.io/','Haifeng Jia'),
    )
    (ROOT/'index.html').write_text(rendered,encoding='utf-8')
    (ROOT/'publications.bib').write_text('\n\n'.join(bibtex(x) for x in pubs)+'\n',encoding='utf-8')
    print(f'Built {ROOT / "index.html"} ({len(pubs)} selected publications).')
    print('Open index.html in your browser to preview. No web server is required.')

if __name__=='__main__':
    try: build()
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print(f'Build failed: {exc}',file=sys.stderr)
        sys.exit(1)
