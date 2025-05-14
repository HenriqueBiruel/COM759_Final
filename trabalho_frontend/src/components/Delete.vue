<template>
  <body>
    <div id="delete-container">
      <form @submit.prevent="deleteMidia">
        <div id="container">
          <div id="titulo">
            <h1>Deletar Mídia</h1>
          </div>

          <div class="delete-form">
            <div class="caixa">
              <div class="form-group">
                <label for="midia_id">ID</label>
                <input
                  type="text"
                  class="form-control"
                  disabled
                  v-model="midia.id"
                  id="midia_id"
                />
              </div>

              <div class="form-group">
                <label for="midia_titulo">Título</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="midia.titulo"
                  id="midia_titulo"
                  disabled
                />
              </div>

              <div class="form-group">
                <label for="midia_tipo">Tipo</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="midia.tipo"
                  id="midia_tipo"
                  disabled
                />
              </div>

              <div class="form-group">
                <label for="midia_genero">Gênero</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="midia.genero"
                  id="midia_genero"
                  disabled
                />
              </div>

              <div class="form-group">
                <label for="midia_ano">Ano</label>
                <input
                  type="number"
                  class="form-control"
                  v-model="midia.ano"
                  id="midia_ano"
                  disabled
                />
              </div>

              <div class="form-group">
                <label for="midia_avaliacao">Avaliação</label>
                <input
                  type="number"
                  class="form-control"
                  v-model="midia.avaliacao"
                  id="midia_avaliacao"
                  disabled
                />
              </div>

              <div class="form-group">
                <label for="midia_descricao">Descrição</label>
                <textarea
                  class="form-control"
                  v-model="midia.descricao"
                  id="midia_descricao"
                  disabled
                ></textarea>
              </div>

              <div class="form-group">
                <button class="btn btn-danger">Deletar</button>
              </div>

              <div id="voltar-link">
                <p>
                  <router-link :to="{ name: 'list' }">
                    Voltar para a lista de Filmes e Séries
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
import '../assets/update.css';

export default {
  data() {
    return {
      midia: {}
    };
  },
  created() {
    this.getMidiaData();
  },
  methods: {
    getMidiaData() {
      this.$http
        .get(`http://localhost:5000/getid/${this.$route.params.id}`)
        .then(
          (response) => {
            this.midia.id = this.$route.params.id;
            this.midia.titulo = response.body.titulo;
            this.midia.tipo = response.body.tipo;
            this.midia.genero = response.body.genero;
            this.midia.ano = response.body.ano;
            this.midia.avaliacao = response.body.avaliacao;
            this.midia.descricao = response.body.descricao;
            this.$forceUpdate();
          },
          () => {
            alert("Erro ao buscar dados da mídia.");
          }
        );
    },
    deleteMidia() {
      this.$http.get(`http://localhost:5000/delete/${this.midia.id}`).then(
        (response) => {
          this.midia = {};
          alert(response.body.mensagem);
          this.$router.push("list");
        },
        (response) => {
          alert(response.body.mensagem);
        }
      );
    }
  }
};
</script>
