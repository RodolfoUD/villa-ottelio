import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import compress from 'astro-compress';

// Migrazione villaottelio.it: sito HTML statico (Vite+Tailwind CDN) -> Astro.
// - build.format: 'preserve' -> rispetta la struttura dei file sorgente:
//   the-manor.astro -> the-manor.html, it/index.astro -> it/index.html.
//   Mantiene ESATTAMENTE gli URL del sito esistente (anche /it/index.html).
// - Tailwind compilato a build time (@astrojs/tailwind): elimina il CDN
//   cdn.tailwindcss.com (anti-pattern in produzione).
// - i18n: en alla root, it/ de/ fr/ nl/ zh/ come sottocartelle.
export default defineConfig({
  site: 'https://www.villaottelio.it',
  build: {
    format: 'preserve',
  },
  integrations: [
    tailwind(),
    compress({ CSS: true, HTML: true, JavaScript: true, Image: false, SVG: false }),
  ],
});
