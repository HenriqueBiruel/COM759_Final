<template>
  <div id="cadastro">
    <h1>Cadastro de Usuário</h1>

    <p>
      <router-link :to="{ name: 'login' }">Já tem uma conta? Faça login</router-link>
    </p>

    <form v-on:submit.prevent="cadastrarUsuario">
      <div class="form-group">
        <label for="username">Usuário</label>
        <input
          type="text"
          id="username"
          class="form-control"
          v-model="usuario.username"
          required
        />
      </div>

      <div class="form-group">
        <label for="password">Senha</label>
        <input
          type="password"
          id="password"
          class="form-control"
          v-model="usuario.password"
          required
        />
      </div>

      <div class="form-group">
        <button class="btn btn-primary">Cadastrar</button>
      </div>
    </form>
  </div>
</template>

<script>
import '../assets/cadastro.css';

export default {
  data() {
    return {
      usuario: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    cadastrarUsuario() {
      this.$http
        .post('http://localhost:5000/cadastro', this.usuario, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            alert(response.body.mensagem)
            this.$router.push({ name: 'login' }) // Redireciona para a página de login
          },
          (error) => {
            alert(error.body.mensagem)
          }
        )
    }
  }
}
</script>