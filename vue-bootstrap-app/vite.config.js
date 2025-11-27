import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { fileURLToPath, URL } from 'node:url';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  css: {
    preprocessorOptions: {
      scss: {
        // REMOVIDO: A linha abaixo é a causa provável do seu erro.
        // Deixe 'additionalData' vazio ou comente-o para evitar a auto-importação.
        // additionalData: `@import "@/assets/styles/custom.scss";`
      },
    },
  },
});