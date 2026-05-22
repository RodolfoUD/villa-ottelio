# Report — villaottelio.it: migrazione ad Astro

Data: 22/05/2026.

## Esito

Sito `www.villaottelio.it` migrato da HTML statico (Vite + Tailwind CDN)
ad **Astro**. **244 pagine**, 6 lingue, build verde, **URL invariati**.
Eliminato il CDN Tailwind — la causa che ostacolava l'indicizzazione.

## Cartelle

| | Path |
|---|---|
| Sorgente (intatta, sola lettura) | `C:\Users\rdeca\villa-ottelio\` |
| Progetto Astro | `C:\Users\rdeca\villa-ottelio-astro\` |

## Cosa è stato fatto

- **Eliminato `cdn.tailwindcss.com`** (Tailwind Play CDN, sconsigliato in
  produzione: CSS generato a runtime da JavaScript). Ora Tailwind è
  **compilato a build time** (`@astrojs/tailwind`) → CSS statico reale
  in `_astro/*.css`, nessuna dipendenza JS per lo stile.
- Eliminato Vite e il `/src/style.css` con `@tailwind` non compilato.
- `build.format: 'preserve'` → ogni URL `.html` invariato
  (`/the-manor.html`, `/it/dimora.html`, `/blog/...`). Parità 244/244.
- **Componenti condivisi**: `Layout` (head, GA4 `G-TFTR0GE584`, cookie
  banner, font), `Header` (nav + selettore 6 lingue), `Footer` —
  generati da `src/data/site.js`.
- **243 pagine `.astro`** generate dal contenuto dei file HTML originali;
  `og:*`, `twitter:*`, JSON-LD e hreflang **preservati verbatim** per
  pagina. La pagina di verifica Google è ridotta al solo token.
- Font Playfair Display + Inter ora caricati (il sito originale li
  dichiarava nel CSS ma non li importava).

## Lingue (6) — 244 file

en (40) · it (41) · de (41) · fr (41) · nl (40) · zh (41).
Per lingua: ~8 pagine fisse + ~32 blog post. en alla root, le altre in
sottocartelle `it/ de/ fr/ nl/ zh/`.

## Verifica

- **URL**: 244 file originali, 244 nel build — 0 mancanti, 0 in più.
- **canonical**: tutte self-referenti (0 errate); 1 senza canonical =
  file di verifica Google (corretto).
- **hreflang**: dichiarati in un solo posto, le `sitemap-<lang>.xml`
  (6 lingue + x-default per ogni URL, con self-reference). Rimossi
  dall'`<head>` HTML per non avere segnali duplicati.
- **trailing slash**: `loc` sitemap, `canonical` e `og:url` identici —
  home con `/` finale, pagine `.html` senza. Nessun `/index.html`.
- **CDN Tailwind**: 0 pagine.
- Build Astro verde, 243 pagine, `dist/` ≈ 18 MB.

## Deploy (GitHub Pages)

Il sito è su GitHub Pages (file `CNAME` = `www.villaottelio.it`,
incluso in `public/` → finisce in `dist/`).

Workflow pronto: `.github/workflows/deploy.yml` (build Astro +
`actions/deploy-pages`). Per attivarlo:
1. Pubblica questo progetto come repo GitHub.
2. Repo → Settings → Pages → Source = **GitHub Actions**.
3. Ogni push su `main` builda e pubblica.

In alternativa, build locale e pubblicazione manuale di `dist/`:
```
npm install
npm run build      # genera dist/
npm run preview    # test locale
```

## Note

- Le immagini erano referenziate come `/public/assets/...` (il nome
  della cartella finiva nell'URL). Riscritte in `/assets/...` — URL
  immagine più pulito; le pagine HTML restano agli stessi URL.
- Sorgente `villa-ottelio` non modificata.
