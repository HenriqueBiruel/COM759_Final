<template>
  <body>
    <div id="update-container">
      <form @submit.prevent="updateFilme">
        <div id="container">
          <div id="titulo">
            <h1>Atualizar Midia</h1>
          </div>

          <div class="update-form">
            <div class="caixa">
              <div class="form-group">
                <label for="filme_id">ID</label>
                <input
                  type="text"
                  class="form-control"
                  disabled
                  v-model="filme.id"
                  id="filme_id"
                />
              </div>

              <div class="form-group">
                <label for="filme_titulo">Título</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="filme.titulo"
                  id="filme_titulo"
                  required
                />
              </div>

              <div class="form-group">
                <label for="filme_tipo">Tipo</label>
                <select v-model="filme.tipo" id="filme_tipo" required>
                  <option value="" disabled>Selecione o tipo</option>
                  <option value="Filme">Filme</option>
                  <option value="Série">Série</option>
                </select>
              </div>

              <div class="form-group">
                <label for="filme_genero">Gênero</label>
                <input
                  type="text"
                  class="form-control"
                  v-model="filme.genero"
                  id="filme_genero"
                  required
                />
              </div>

              <div class="form-group">
                <label for="filme_ano">Ano</label>
                <input
                  type="number"
                  class="form-control"
                  v-model="filme.ano"
                  id="filme_ano"
                  min="1900"
                  max="2025"
                  required
                />
              </div>

              <div class="form-group">
                <label for="filme_avaliacao">Avaliação</label>
                <input
                  type="number"
                  class="form-control"
                  v-model="filme.avaliacao"
                  id="filme_avaliacao"
                  min="0"
                  max="10"
                  step="0.1"
                  required
                />
              </div>

              <div class="form-group">
                <label for="filme_descricao">Descrição</label>
                <textarea
                  class="form-control"
                  v-model="filme.descricao"
                  id="filme_descricao"
                  required
                ></textarea>
              </div>

              <div class="form-group">
                <button class="btn btn-primary">Atualizar</button>
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
      filme: {}
    };
  },
  created() {
    this.getFilmeData();
  },
  methods: {
    getFilmeData() {
      this.$http
        .get(`http://localhost:5000/getid/${this.$route.params.id}`)
        .then(
          (response) => {
            this.filme.id = this.$route.params.id;
            this.filme.titulo = response.body.titulo;
            this.filme.tipo = response.body.tipo;
            this.filme.genero = response.body.genero;
            this.filme.ano = response.body.ano;
            this.filme.avaliacao = response.body.avaliacao;
            this.filme.descricao = response.body.descricao;
            this.$forceUpdate();
          },
          () => {
            alert("Erro ao buscar dados do filme.");
          }
        );
    },
    updateFilme() {
      // Validação
      const ano = parseInt(this.filme.ano, 10);
      const avaliacao = parseFloat(this.filme.avaliacao);

      if (isNaN(ano) || ano < 1900 || ano > 2025) {
        alert("Ano deve ser um número entre 1900 e 2025.");
        return;
      }

      if (isNaN(avaliacao) || avaliacao < 0 || avaliacao > 10) {
        alert("Avaliação deve ser um número entre 0 e 10.");
        return;
      }

      this.$http
        .post("http://localhost:5000/update", this.filme, {
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(
          (response) => {
            this.filme = {};
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
