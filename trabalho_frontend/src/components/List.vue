
<template>
  <body>
    <div id="list-container">
      <div id="top-bar">
        <div class="top-bar-buttons">
          <router-link :to="{ name: 'perfil' }" class="top-button">Meu Perfil</router-link>
          <button @click="logout" class="top-button">Logout</button>
        </div>
      </div>

      <div id="container">
        <div id="titulo">
          <h1>Lista de Filmes e Séries</h1>
        </div>

        <div class="list-form">
          <p>
            <router-link :to="{ name: 'create' }" class="btn btn-primary">
              Cadastrar Novo Filme ou Série
            </router-link>
          </p>

          <table class="table table-hover">
            <thead>
              <tr>
                <th>Pôster</th>
                <th>Título</th>
                <th>Tipo</th>
                <th>Gênero</th>
                <th>Ano</th>
                <th>Avaliação</th>
                <th>Descrição</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="midia in midias" :key="midia._id['$oid']">
                <td>
                  <img
                    :src="midia.imagem || 'https://via.placeholder.com/70x100?text=Sem+Imagem'"
                    alt="Poster"
                    style="width: 70px; height: 100px; object-fit: cover; border-radius: 4px;"
                  />
                </td>
                <td>{{ midia.titulo }}</td>
                <td>{{ midia.tipo }}</td>
                <td>{{ midia.genero }}</td>
                <td>{{ midia.ano }}</td>
                <td>{{ midia.avaliacao }}</td>
                <td>{{ midia.descricao }}</td>
                <td>
                <div class="botoes-acao">
                  <router-link
                    :to="{ name: 'update', params: { id: midia._id['$oid'] } }"
                    class="btn btn-primary"
                  >
                    Editar
                  </router-link>
                  <router-link
                    :to="{ name: 'delete', params: { id: midia._id['$oid'] } }"
                    class="btn btn-danger"
                  >
                    Excluir
                  </router-link>
                </div>
              </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </body>
</template>

<script>
import '../assets/list.css'

export default {
  data () {
    return {
      midias: []
    }
  },
  created () {
    const userId = localStorage.getItem('user_id')
    if (!userId) {
      alert('Usuário não identificado. Faça login novamente.')
      this.$router.push({ name: 'login' })
      return
    }
    this.fetchMidiaData()
  },

  methods: {
    fetchMidiaData () {
      const userId = localStorage.getItem('user_id')
      this.$http.get(`http://localhost:5000/list/${userId}`).then(
        (response) => {
          this.midias = response.body
        },
        (response) => {
          console.error('Erro ao buscar dados das mídias:', response)
        }
      )
    },
    logout () {
      localStorage.removeItem('username')
      localStorage.removeItem('user_id')
      this.$router.push({ name: 'login' })
    }

  }
}
</script>
