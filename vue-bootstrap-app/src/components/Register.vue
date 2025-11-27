<template>
  <div class="container mt-4">
    <h2>Registrar</h2>
    <form @submit.prevent="register" novalidate>
      <div class="mb-3" v-for="(value, key) in form" :key="key">
        <label class="form-label" :for="key">{{ labels[key] || key }}</label>
        <input v-model="form[key]" :id="key" class="form-control" />
        <div v-if="errors[key]" class="text-danger small">{{ errors[key] }}</div>
      </div>
      <button type="submit" class="btn btn-primary">Criar conta</button>
      <button type="button" @click="$emit('show-login')" class="btn btn-link">Já tenho conta</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'RegisterForm',
  data() {
    return {
      form: { username: '', email: '', password1: '', password2: '' },
      labels: { username: 'Usuário', email: 'Email', password1: 'Senha', password2: 'Confirmar senha' },
      errors: {}
    };
  },
  methods: {
    async register() {
      this.errors = {};
      try {
        const res = await axios.post('/register/', this.form);
        if (res.data?.success) {
          // sucesso
        } else if (res.data?.errors) {
          this.errors = res.data.errors;
        }
      } catch (err) {
        this.errors.non_field = err.response?.data || 'Erro';
      }
    }
  }
};
</script>