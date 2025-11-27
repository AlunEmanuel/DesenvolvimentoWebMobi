// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Sistema from '../components/Sistema.vue';
import Veiculos from '../components/Veiculos.vue';
import VehicleForm from '../components/VehicleForm.vue'; // Importe o componente de formulário

const routes = [
  { path: '/', name: 'Home', component: Sistema },
  // Rotas de Veículos
  { path: '/veiculos', name: 'listar-veiculos', component: Veiculos },
  
  // AQUI: Alterar para usar VehicleForm.vue em vez de Veiculos.vue
  { path: '/veiculos/novo', name: 'VeiculosNovo', component: VehicleForm },
  
  { path: '/cadastrar', redirect: '/veiculos/novo' },
  
  // Redirecionamento padrão para home se a rota não existir
  { path: '/:pathMatch(.*)*', redirect: '/' }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

export default router;