(function () {
  'use strict';

  const COOKIE_KEY = 'vo_cookie_consent';
  const GA_ID = 'G-TFTR0GE584';

  const texts = {
    it: {
      message: 'Questo sito utilizza cookie analitici (Google Analytics) per migliorare la navigazione. I dati sono trattati in forma aggregata.',
      accept: 'Accetta',
      reject: 'Rifiuta',
      privacy: 'Privacy Policy',
      privacyUrl: '/it/privacy.html'
    },
    en: {
      message: 'This site uses analytical cookies (Google Analytics) to improve navigation. Data is processed in aggregate form.',
      accept: 'Accept',
      reject: 'Decline',
      privacy: 'Privacy Policy',
      privacyUrl: '/privacy-policy.html'
    },
    fr: {
      message: 'Ce site utilise des cookies analytiques (Google Analytics) pour améliorer la navigation. Les données sont traitées sous forme agrégée.',
      accept: 'Accepter',
      reject: 'Refuser',
      privacy: 'Politique de Confidentialité',
      privacyUrl: '/fr/politique-confidentialite.html'
    },
    de: {
      message: 'Diese Website verwendet Analyse-Cookies (Google Analytics) zur Verbesserung der Navigation. Daten werden in aggregierter Form verarbeitet.',
      accept: 'Akzeptieren',
      reject: 'Ablehnen',
      privacy: 'Datenschutz',
      privacyUrl: '/de/datenschutz.html'
    },
    nl: {
      message: 'Deze website gebruikt analytische cookies (Google Analytics) om de navigatie te verbeteren. Gegevens worden in geaggregeerde vorm verwerkt.',
      accept: 'Accepteren',
      reject: 'Weigeren',
      privacy: 'Privacybeleid',
      privacyUrl: '/nl/privacybeleid.html'
    },
    zh: {
      message: '本网站使用分析性Cookie（Google Analytics）以改善浏览体验。数据以汇总形式处理。',
      accept: '接受',
      reject: '拒绝',
      privacy: '隐私政策',
      privacyUrl: '/zh/privacy-policy.html'
    }
  };

  function detectLang() {
    var path = window.location.pathname;
    if (path.startsWith('/it/')) return 'it';
    if (path.startsWith('/fr/')) return 'fr';
    if (path.startsWith('/de/')) return 'de';
    if (path.startsWith('/nl/')) return 'nl';
    if (path.startsWith('/zh/')) return 'zh';
    return 'en';
  }

  function loadGA() {
    if (window._gaLoaded) return;
    window._gaLoaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    function gtag() { dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', GA_ID, { anonymize_ip: true });
  }

  function setConsent(value) {
    try { localStorage.setItem(COOKIE_KEY, value); } catch (e) {}
  }

  function getConsent() {
    try { return localStorage.getItem(COOKIE_KEY); } catch (e) { return null; }
  }

  function removeBanner(banner) {
    banner.style.transform = 'translateY(100%)';
    banner.style.opacity = '0';
    setTimeout(function () {
      if (banner.parentNode) banner.parentNode.removeChild(banner);
    }, 400);
  }

  function createBanner() {
    var lang = detectLang();
    var t = texts[lang] || texts.en;

    var banner = document.createElement('div');
    banner.id = 'vo-cookie-banner';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', t.message);
    banner.style.cssText = [
      'position:fixed',
      'bottom:0',
      'left:0',
      'right:0',
      'z-index:99999',
      'background:#0a0a0a',
      'border-top:1px solid #c5a059',
      'padding:16px 20px',
      'display:flex',
      'flex-wrap:wrap',
      'align-items:center',
      'gap:12px',
      'font-family:Inter,sans-serif',
      'font-size:13px',
      'color:#e5e1d8',
      'line-height:1.5',
      'transform:translateY(0)',
      'opacity:1',
      'transition:transform 0.4s ease, opacity 0.4s ease',
      'box-shadow:0 -2px 20px rgba(0,0,0,0.5)'
    ].join(';');

    var msg = document.createElement('p');
    msg.style.cssText = 'margin:0;flex:1;min-width:200px;';
    msg.textContent = t.message + ' ';

    var privLink = document.createElement('a');
    privLink.href = t.privacyUrl;
    privLink.textContent = t.privacy;
    privLink.style.cssText = 'color:#c5a059;text-decoration:underline;white-space:nowrap;';
    msg.appendChild(privLink);

    var btnWrap = document.createElement('div');
    btnWrap.style.cssText = 'display:flex;gap:10px;flex-shrink:0;';

    var btnAccept = document.createElement('button');
    btnAccept.textContent = t.accept;
    btnAccept.style.cssText = [
      'background:#c5a059',
      'color:#0a0a0a',
      'border:none',
      'padding:9px 22px',
      'font-size:13px',
      'font-weight:700',
      'cursor:pointer',
      'letter-spacing:0.05em',
      'text-transform:uppercase',
      'white-space:nowrap',
      'min-height:44px'
    ].join(';');

    var btnReject = document.createElement('button');
    btnReject.textContent = t.reject;
    btnReject.style.cssText = [
      'background:transparent',
      'color:#e5e1d8',
      'border:1px solid #e5e1d8',
      'padding:9px 22px',
      'font-size:13px',
      'font-weight:400',
      'cursor:pointer',
      'letter-spacing:0.05em',
      'text-transform:uppercase',
      'white-space:nowrap',
      'min-height:44px'
    ].join(';');

    btnAccept.addEventListener('click', function () {
      setConsent('accepted');
      loadGA();
      removeBanner(banner);
    });

    btnReject.addEventListener('click', function () {
      setConsent('rejected');
      removeBanner(banner);
    });

    btnWrap.appendChild(btnReject);
    btnWrap.appendChild(btnAccept);
    banner.appendChild(msg);
    banner.appendChild(btnWrap);

    return banner;
  }

  function init() {
    var consent = getConsent();
    if (consent === 'accepted') {
      loadGA();
      return;
    }
    if (consent === 'rejected') {
      return;
    }
    // Nessuna scelta ancora — mostra banner
    document.body.appendChild(createBanner());
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();