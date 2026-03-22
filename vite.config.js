import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        it_index: resolve(__dirname, 'src/it/index.html'),
        it_parco: resolve(__dirname, 'src/it/parco.html'),
        it_dimora: resolve(__dirname, 'src/it/dimora.html'),
        it_contatti: resolve(__dirname, 'src/it/contatti.html'),
        it_vegetazione: resolve(__dirname, 'src/it/vegetazione.html'),
        it_magazine: resolve(__dirname, 'src/it/magazine.html'),
        it_investimento: resolve(__dirname, 'src/it/investimento.html'),
        it_privacy: resolve(__dirname, 'src/it/privacy.html')
      }
    }
  }
});
