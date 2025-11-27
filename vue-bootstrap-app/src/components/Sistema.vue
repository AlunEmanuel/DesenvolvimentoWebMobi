<template>
  <div>
    <LoginForm v-if="view === 'login'" />
    <RegisterForm v-if="view === 'register'" @show-login="view = 'login'" />
  </div>
</template>

<script>
import LoginForm from './Login.vue';
import RegisterForm from './Register.vue';
export default {
  name: 'Sistema',
  components: { LoginForm, RegisterForm },
  data() {
    return { view: 'login' };
  }
};
</script>

<style scoped>
/* Adicione estilos locais se necessário; seu custom.scss continua global */
</style>
