<template>
  <div class="card mb-3">
    <div class="row g-0 d-flex align-items-center">
      <div class="col-lg-8">
        <div class="card-body py-5 px-md-5">
          <form @submit.prevent="login">
            <div class="form-outline mb-4">
              <input v-model="email" type="text" class="form-control" />
              <label class="form-label">Email address</label>
            </div>
            <div class="form-outline mb-4">
              <input v-model="password" type="password" class="form-control" />
              <label class="form-label">Password</label>
            </div>
            <div class="row mb-4">
              <div class="col d-flex justify-content-center">
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" v-model="remember" />
                  <label class="form-check-label"> Remember me </label>
                </div>
              </div>
              <div class="col">
                <a href="#!">Forgot password?</a>
              </div>
            </div>
            <button type="submit" class="btn btn-primary btn-block mb-4">Sign in</button>
          </form>

          <div class="mt-3">
            <div v-if="error" class="alert alert-danger">{{ error }}</div>
            <div v-if="message" class="alert alert-info">{{ message }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'LoginForm',
  data() {
    return { email: '', password: '', remember: true, error: '', message: '' };
  },
  methods: {
    async login() {
      this.error = this.message = '';
      try {
        const res = await axios.post('/login/', { email: this.email, password: this.password, remember: this.remember });
        if (res.data?.success) {
          this.message = 'Login bem-sucedido';
          // this.$router.push('/dashboard') ou emitir evento
        } else {
          this.error = res.data?.error || 'Credenciais inválidas';
        }
      } catch (err) {
        this.error = err.response?.data?.error || 'Erro de rede';
      }
    }
  }
};
</script>

<style scoped>
    body {
        background-color: #f8f9fa;
    }

    .container {
        max-width: 200px;
        margin: 0 auto;
        align-items: center;
        justify-content: center;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 5px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    h2 {
        text-align: center;
        margin-bottom: 20px;
    }

    .form-group {
        margin-bottom: 15px;
    }

    .btn-primary {
        width: 100%;
    }
</style>