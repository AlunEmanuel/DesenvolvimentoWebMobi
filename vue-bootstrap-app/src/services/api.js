import axios from 'axios';

const baseURL =
  // Vue CLI
  process.env.VUE_APP_API_URL ||
  // Vite
  (typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.VITE_API_URL) ||
  // fallback
  'http://localhost:3000';

const API = axios.create({
  baseURL,
  // timeout: 10000,
});

// Exemplos de helpers (opcional)
export const getVeiculos = () => API.get('/veiculos');
export const getSistemas = () => API.get('/sistemas');

export default API;
