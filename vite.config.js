import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  publicDir: 'public',

  build: {
    outDir: 'dist',
    rollupOptions: {
      input: {
        // ── CSS globale ────────────────────────────────────
        style:            resolve(__dirname, 'src/style.css'),

        // ── EN (root) ──────────────────────────────────────
        main:             resolve(__dirname, 'index.html'),
        the_manor:        resolve(__dirname, 'the-manor.html'),
        the_park:         resolve(__dirname, 'the-park.html'),
        nature:           resolve(__dirname, 'nature.html'),
        blog:             resolve(__dirname, 'blog.html'),
        investment:       resolve(__dirname, 'investment.html'),
        contact:          resolve(__dirname, 'contact.html'),
        privacy_policy:   resolve(__dirname, 'privacy-policy.html'),
        blog_article_en:  resolve(__dirname, 'src/blog/real-estate-analysis.html'),

        // ── IT ─────────────────────────────────────────────
        it_index:         resolve(__dirname, 'it/index.html'),
        it_dimora:        resolve(__dirname, 'it/dimora.html'),
        it_parco:         resolve(__dirname, 'it/parco.html'),
        it_vegetazione:   resolve(__dirname, 'it/vegetazione.html'),
        it_blog:          resolve(__dirname, 'it/blog.html'),
        it_investimento:  resolve(__dirname, 'it/investimento.html'),
        it_contatti:      resolve(__dirname, 'it/contatti.html'),
        it_privacy:       resolve(__dirname, 'it/privacy.html'),
        it_blog_article:  resolve(__dirname, 'it/blog/analisi-mercato-immobiliare.html'),
      }
    }
  }
});