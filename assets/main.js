/* Progressive enhancement: all biography and publication content is in index.html. */
(() => {
  'use strict';
  const root = document.documentElement;
  root.classList.add('js');
  const languageButton = document.getElementById('language-switch');
  function setLanguage(lang) {
    const chinese = lang === 'zh';
    root.lang = chinese ? 'zh-CN' : 'en';
    if (languageButton) {
      languageButton.textContent = chinese ? 'EN' : '中文';
      languageButton.setAttribute('aria-label', chinese ? 'Switch to English' : '切换为中文');
    }
    document.title = chinese ? '胡发成 · 学术主页' : 'Facheng Hu · Academic Homepage';
    try { localStorage.setItem('fh-homepage-language', lang); } catch (_) { /* Optional storage. */ }
  }
  let language = root.lang.startsWith('zh') ? 'zh' : 'en';
  try {
    const saved = localStorage.getItem('fh-homepage-language');
    if (saved === 'en' || saved === 'zh') language = saved;
  } catch (_) { /* The site works even when storage is blocked. */ }
  setLanguage(language);
  languageButton?.addEventListener('click', () => setLanguage(root.lang.startsWith('zh') ? 'en' : 'zh'));

  let toastTimer;
  function notify(en, zh) {
    const toast = document.getElementById('toast');
    if (!toast) return;
    toast.textContent = root.lang.startsWith('zh') ? zh : en;
    toast.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => { toast.hidden = true; }, 2800);
  }
  async function copyText(text) {
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(text);
        return true;
      }
    } catch (_) { /* Fall back to local-file compatible selection below. */ }
    const area = document.createElement('textarea');
    area.value = text;
    area.setAttribute('readonly', '');
    area.style.cssText = 'position:fixed;top:-9999px;left:-9999px';
    document.body.append(area);
    area.select();
    let ok = false;
    try { ok = document.execCommand('copy'); } catch (_) { /* Keep failure visible. */ }
    area.remove();
    return ok;
  }
  document.querySelectorAll('[data-copy]').forEach(button => {
    button.addEventListener('click', async () => {
      const text = button.dataset.copy || '';
      const ok = await copyText(text);
      if (ok) notify('Email address copied.', '邮箱地址已复制。');
      else notify('Please select and copy the email address.', '请选中邮箱地址后手动复制。');
    });
  });
  document.querySelectorAll('[data-copy-citation]').forEach(button => {
    button.addEventListener('click', async () => {
      const code = document.getElementById(button.dataset.copyCitation);
      if (!code) return;
      const ok = await copyText(code.textContent);
      if (ok) notify('BibTeX copied.', 'BibTeX 已复制。');
      else notify('Please select and copy the citation text.', '请选中引用文本后手动复制。');
    });
  });
  const filters = document.querySelectorAll('[data-filter]');
  const papers = document.querySelectorAll('.publication-card');
  filters.forEach(button => {
    button.addEventListener('click', () => {
      const year = button.dataset.filter;
      filters.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
      let visible = 0;
      papers.forEach(paper => {
        paper.hidden = year !== 'all' && paper.dataset.year !== year;
        if (!paper.hidden) visible++;
      });
      const message = document.getElementById('filter-status');
      if (message) message.textContent = root.lang.startsWith('zh') ? `显示 ${visible} 篇论文` : `${visible} publications shown`;
    });
  });
  // Update header navigation as the corresponding section enters the viewport.
  if ('IntersectionObserver' in window) {
    const navLinks = [...document.querySelectorAll('.header-nav a[href^="#"]')];
    const observer = new IntersectionObserver(entries => {
      const current = entries.filter(x => x.isIntersecting).sort((a,b) => b.intersectionRatio-a.intersectionRatio)[0];
      if (!current) return;
      navLinks.forEach(a => {
        if (a.hash === '#' + current.target.id) a.setAttribute('aria-current', 'location');
        else a.removeAttribute('aria-current');
      });
    }, {rootMargin: '-70px 0px -45% 0px', threshold: [0, .1, .4]});
    navLinks.forEach(a => { const section=document.querySelector(a.hash); if(section) observer.observe(section); });
  }
  document.querySelectorAll('img[data-portrait]').forEach(img => {
    img.addEventListener('error', () => {
      const frame = img.parentElement;
      img.remove();
      frame.classList.remove('has-photo');
      const initials = document.createElement('span');
      initials.className = 'monogram';
      initials.textContent = frame.dataset.initials || 'FH';
      frame.append(initials);
    });
  });
})();
