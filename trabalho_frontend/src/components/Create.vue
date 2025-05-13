<template>
  <body>
    <div id="create-container">
      <form @submit.prevent="addMidia">
        <div id="container">
          <div id="titulo">
            <h1>Gestão de Filmes</h1>
          </div>

          <div class="create-form">
            <h2>Cadastrar Mídia</h2>

            <div class="create-caixa">
              <div class="titulo">
                <input
                  type="text"
                  placeholder="Título"
                  v-model="midia.titulo"
                  required
                />
              </div>

              <div class="tipo">
                <select v-model="midia.tipo" required>
                  <option value="" disabled selected>Selecione o tipo</option>
                  <option value="Filme">Filme</option>
                  <option value="Série">Série</option>
                </select>
              </div>

              <div class="genero">
                <input
                  type="text"
                  placeholder="Gênero"
                  v-model="midia.genero"
                  required
                />
              </div>

              <div class="ano">
                <input
                  type="number"
                  placeholder="Ano"
                  v-model="midia.ano"
                  required
                />
              </div>

              <div class="descricao">
                <textarea
                  placeholder="Descrição"
                  v-model="midia.descricao"
                  required
                ></textarea>
              </div>

              <div class="avaliacao">
                <input
                  type="number"
                  step="0.1"
                  placeholder="Avaliação"
                  v-model="midia.avaliacao"
                  required
                />
              </div>

              <div class="entrar">
                <input type="submit" id="login-btn" value="Cadastrar" />
              </div>

              <div id="cadastro-link">
                <p>
                  <router-link :to="{ name: 'list' }">
                    Voltar para a lista de mídias
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
import '../assets/global.css';

export default {
  data() {
    return {
      midia: {
        titulo: '',
        tipo: '',
        genero: '',
        ano: '',
        descricao: '',
        avaliacao: ''
      }
    };
  },
  methods: {
    addMidia() {
      this.$http
        .post('http://localhost:5000/create', this.midia, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            this.midia = {};
            alert(response.body.mensagem);
            this.$router.push({ name: 'list' });
          },
          (error) => {
            alert((error.body && error.body.mensagem) || 'Erro ao cadastrar mídia');
          }
        );
    }
  }
};
</script>
