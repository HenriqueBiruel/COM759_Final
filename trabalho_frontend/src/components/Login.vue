
<template>
  <body>
    <div id="login-container">
      <form @submit.prevent="fazerLogin">
        <div id="container">
          <div id="titulo">
            <h1>Gestão de Filmes e Séries</h1>
          </div>

          <div class="login-form">
            <h2>Login</h2>

            <div class="caixa">
              <div class="usuario">
                <input type="text" placeholder="Usuário" v-model="usuario.username" required />
              </div>

              <div class="senha">
                <input type="password" placeholder="Senha" v-model="usuario.password" required />
              </div>

              <div class="entrar">
                <input type="submit" id="login-btn" value="Entrar" />
              </div>

              <div id="cadastro-link">
                <p>
                  <router-link :to="{ name: 'cadastro' }">
                    Não tem uma conta? Cadastre-se
                  </router-link>
                </p>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
  </body>
</template>

<script>
import '../assets/global.css'

export default {
  data () {
    return {
      usuario: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    fazerLogin () {
      this.$http
        .post('http://localhost:5000/login', this.usuario, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            alert(response.body.mensagem)

            // Sempre salva o username no localStorage
            localStorage.setItem('user_id', response.body._id)

            this.$router.push({ name: 'list' })
          },
          (error) => {
            alert((error.body && error.body.mensagem) || 'Erro ao fazer login')
          }
        )
    }
  }
}
</script>
