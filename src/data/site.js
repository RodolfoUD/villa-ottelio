// site.js — configurazione per lingua di villaottelio.it
export const GA_ID = 'G-TFTR0GE584';
export const LANGS = ['en', 'it', 'de', 'fr', 'nl', 'zh'];

// Bandiera flag-icons + etichetta per il selettore lingua
export const langMeta = {
  en: { flag: 'fi-gb', label: 'EN' },
  it: { flag: 'fi-it', label: 'IT' },
  de: { flag: 'fi-de', label: 'DE' },
  fr: { flag: 'fi-fr', label: 'FR' },
  nl: { flag: 'fi-nl', label: 'NL' },
  zh: { flag: 'fi-cn', label: 'ZH' },
};

// nav: ogni voce ha `key` (per lo stato attivo) + label + href.
// footer: copyright + link.
export const site = {
  en: {
    htmlLang: 'en',
    nav: [
      { key: 'home', label: 'Home', href: '/' },
      { key: 'manor', label: 'The Manor', href: '/the-manor.html' },
      { key: 'park', label: 'The Park', href: '/the-park.html' },
      { key: 'nature', label: 'Nature', href: '/nature.html' },
      { key: 'blog', label: 'Diary', href: '/blog.html' },
      { key: 'investment', label: 'Investment', href: '/investment.html' },
      { key: 'contact', label: 'Contact', href: '/contact.html' },
    ],
    footer: {
      copyright: '© 2026 Villa Ottelio de Carvalho. All rights reserved.',
      links: [
        { label: 'Privacy Policy', href: '/privacy-policy.html' },
        { label: 'Request a Visit', href: '/contact.html' },
      ],
    },
  },
  it: {
    htmlLang: 'it',
    nav: [
      { key: 'home', label: 'Home', href: '/it/' },
      { key: 'manor', label: 'La Dimora', href: '/it/dimora.html' },
      { key: 'park', label: 'Il Parco', href: '/it/parco.html' },
      { key: 'nature', label: 'Botanica', href: '/it/vegetazione.html' },
      { key: 'blog', label: 'Diario', href: '/it/blog.html' },
      { key: 'investment', label: 'Investimento', href: '/it/investimento.html' },
      { key: 'contact', label: 'Contatti', href: '/it/contatti.html' },
    ],
    footer: {
      copyright: '© 2026 Villa Ottelio de Carvalho. Tutti i diritti riservati.',
      links: [
        { label: 'Privacy Policy', href: '/it/privacy.html' },
        { label: 'Richiedi Visita', href: '/it/contatti.html' },
      ],
    },
  },
  de: {
    htmlLang: 'de',
    nav: [
      { key: 'home', label: 'Home', href: '/de/' },
      { key: 'manor', label: 'Das Anwesen', href: '/de/anwesen.html' },
      { key: 'park', label: 'Der Park', href: '/de/park.html' },
      { key: 'nature', label: 'Botanik', href: '/de/botanik.html' },
      { key: 'blog', label: 'Blog', href: '/de/blog.html' },
      { key: 'investment', label: 'Investition', href: '/de/investition.html' },
      { key: 'contact', label: 'Kontakt', href: '/de/kontakt.html' },
    ],
    footer: {
      copyright: '© 2026 Villa Ottelio de Carvalho. Alle Rechte vorbehalten.',
      links: [
        { label: 'Datenschutz', href: '/de/datenschutz.html' },
        { label: 'Kontakt', href: '/de/kontakt.html' },
      ],
    },
  },
  fr: {
    htmlLang: 'fr',
    nav: [
      { key: 'home', label: 'Home', href: '/fr/' },
      { key: 'manor', label: 'Le Manoir', href: '/fr/le-manoir.html' },
      { key: 'park', label: 'Le Parc', href: '/fr/le-parc.html' },
      { key: 'nature', label: 'Botanique', href: '/fr/nature.html' },
      { key: 'blog', label: 'Journal', href: '/fr/blog.html' },
      { key: 'investment', label: 'Investissement', href: '/fr/investissement.html' },
      { key: 'contact', label: 'Contact', href: '/fr/contact.html' },
    ],
    footer: {
      copyright: '© 2026 Villa Ottelio de Carvalho. Tous droits réservés.',
      links: [
        { label: 'Politique de Confidentialité', href: '/fr/politique-confidentialite.html' },
        { label: 'Demander une Visite', href: '/fr/contact.html' },
      ],
    },
  },
  nl: {
    htmlLang: 'nl',
    nav: [
      { key: 'home', label: 'Home', href: '/nl/' },
      { key: 'manor', label: 'Het Landhuis', href: '/nl/landhuis.html' },
      { key: 'park', label: 'Het Park', href: '/nl/park.html' },
      { key: 'nature', label: 'Botanica', href: '/nl/botanica.html' },
      { key: 'blog', label: 'Dagboek', href: '/nl/blog.html' },
      { key: 'investment', label: 'Investering', href: '/nl/investering.html' },
      { key: 'contact', label: 'Contact', href: '/nl/contact.html' },
    ],
    footer: {
      copyright: '© 2026 Villa Ottelio de Carvalho. Alle rechten voorbehouden.',
      links: [
        { label: 'Privacybeleid', href: '/nl/privacybeleid.html' },
        { label: 'Bezoek aanvragen', href: '/nl/contact.html' },
      ],
    },
  },
  zh: {
    htmlLang: 'zh',
    nav: [
      { key: 'home', label: '首页', href: '/zh/' },
      { key: 'manor', label: '庄园', href: '/zh/the-estate.html' },
      { key: 'park', label: '花园', href: '/zh/the-garden.html' },
      { key: 'nature', label: '植物学', href: '/zh/nature.html' },
      { key: 'blog', label: '博客', href: '/zh/blog.html' },
      { key: 'investment', label: '投资', href: '/zh/investment.html' },
      { key: 'contact', label: '联系', href: '/zh/contact.html' },
    ],
    footer: {
      copyright: '© 2026 Villa Ottelio de Carvalho. 版权所有。',
      links: [
        { label: '隐私政策', href: '/zh/privacy-policy.html' },
        { label: '请求参观', href: '/zh/contact.html' },
      ],
    },
  },
};
