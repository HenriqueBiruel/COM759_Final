<template>
  <body>
    <div id="cadastro-container">
      <form @submit.prevent="cadastrarUsuario">
        <div id="container">
          <div id="titulo">
            <h1>Gestão de Filmes</h1>
          </div>

          <div class="cadastro-form">
            <h2>Cadastro</h2>

            <div class="caixa">
              <div class="usuario">
                <input
                  type="text"
                  placeholder="Usuário"
                  v-model="usuario.username"
                  required
                />
              </div>

              <div class="senha">
                <input
                  type="password"
                  placeholder="Senha"
                  v-model="usuario.password"
                  required
                />
              </div>

              <div class="entrar">
                <input type="submit" id="login-btn" value="Cadastrar" />
              </div>

              <div id="cadastro-link">
                <p>
                  <router-link :to="{ name: 'login' }">
                    Já tem uma conta? Faça login
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

export default {
  data() {
    return {
      usuario: {
        username: '',
        password: ''
      }
    };
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
            alert(response.body.mensagem);
            this.$router.push({ name: 'login' }); // Redireciona para a página de login
          },
          (error) => {
            alert((error.body && error.body.mensagem) || 'Erro ao cadastrar');
          }
        );
    }
  }
};
</script>