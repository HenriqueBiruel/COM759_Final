<template>
  <div id="create-midia">
    <h1>Cadastrar Mídia</h1>

    <p>
      <router-link :to="{ name: 'list' }">Voltar para a lista de mídias</router-link>
    </p>
    <form v-on:submit.prevent="addMidia">
      <div class="form-group">
        <label>Título</label>
        <input type="text" class="form-control" v-model="midia.titulo" required />
      </div>

      <div class="form-group">
        <label>Tipo</label>
        <select class="form-control" v-model="midia.tipo" required>
          <option value="Filme">Filme</option>
          <option value="Série">Série</option>
        </select>
      </div>

      <div class="form-group">
        <label>Gênero</label>
        <input type="text" class="form-control" v-model="midia.genero" required />
      </div>

      <div class="form-group">
        <label>Ano</label>
        <input type="number" class="form-control" v-model="midia.ano" required />
      </div>

      <div class="form-group">
        <label>Descrição</label>
        <textarea class="form-control" v-model="midia.descricao" required></textarea>
      </div>

      <div class="form-group">
        <label>Avaliação</label>
        <input type="number" step="0.1" class="form-control" v-model="midia.avaliacao" required />
      </div>

      <div class="form-group">
        <button class="btn btn-primary">Cadastrar</button>
      </div>
    </form>
  </div>
</template>

<script>
import '../assets/create.css';

export default {
  data() {
    return {
      midia: {}
    };
  },
  methods: {
    addMidia: function () {
      this.$http
        .post("http://localhost:5000/create", this.midia, {
          headers: {
            "Content-Type": "application/json"
          }
        })
        .then(
          (response) => {
            this.midia = {};
            alert(response.body["mensagem"]);
            this.$router.push("list");
          },
          (response) => {
            alert(response.body["mensagem"]);
          }
        );
    }
  }
};
</script>
