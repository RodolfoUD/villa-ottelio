import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(process.cwd(), 'index.html'),
      }
    },
    cssMinify: true,
  },
  server: {
    port: 3000,
    open: true,
  }
});