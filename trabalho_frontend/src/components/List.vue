<template>
  <div id="list-midias">
    <h1>Lista de Mídias</h1>

    <p>
      <router-link :to="{ name: 'create' }" class="btn btn-primary">Cadastrar Nova Mídia</router-link>
    </p>
    <table class="table table-hover">
      <thead>
        <tr>
          <td>ID</td>
          <td>Título</td>
          <td>Tipo</td>
          <td>Gênero</td>
          <td>Ano</td>
          <td>Avaliação</td>
          <td>Ações</td>
        </tr>
      </thead>

      <tbody>
        <tr v-for="midia in midias" :key="midia._id['$oid']">
          <td>{{ midia._id['$oid'] }}</td>
          <td>{{ midia.titulo }}</td>
          <td>{{ midia.tipo }}</td>
          <td>{{ midia.genero }}</td>
          <td>{{ midia.ano }}</td>
          <td>{{ midia.avaliacao }}</td>
          <td>
            <router-link :to="{ name: 'update', params: { id: midia._id['$oid'] } }" class="btn btn-primary">Editar</router-link>
            <router-link :to="{ name: 'delete', params: { id: midia._id['$oid'] } }" class="btn btn-danger">Excluir</router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      midias: []
    };
  },
  created: function () {
    this.fetchMidiaData();
  },
  methods: {
    fetchMidiaData: function () {
      this.$http.get("http://localhost:5000/index").then(
        (response) => {
          this.midias = response.body;
        },
        (response) => {}
      );
    }
  }
};
</script>
