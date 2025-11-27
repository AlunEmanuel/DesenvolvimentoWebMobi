import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import './assets/styles/custom.scss';
import Sistema from './components/Sistema.vue';
import Veiculos from './components/Veiculos.vue';

createApp(App)
  .use(router)
  .component('Sistema', Sistema)
  .component('Veiculos', Veiculos)
  .mount('#app');