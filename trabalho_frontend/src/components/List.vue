<template>
    <div id="list-usuarios">
      <h1>List Usuários</h1>
  
      <p>
        <router-link :to="{ name: 'create' }" class="btn btn-primary"
          >Create Usuário</router-link
        >
      </p>
      <table class="table table-hover">
        <thead>
          <tr>
            <td>ID</td>
            <td>Nome</td>
            <td>E-mail</td>
            <td>Idade</td>
          </tr>
        </thead>
  
        <tbody>
          <tr v-for='usuario in usuarios' v-bind:key='usuario'>
            <td>{{ usuario._id['$oid'] }}</td>
            <td>{{ usuario.nome }}</td>
            <td>{{ usuario.email }}</td>
            <td>{{ usuario.idade }}</td>
            <td>
              <router-link
                :to="{ name: 'update', params: { id: usuario._id['$oid'] } }"
                class="btn btn-primary"
                >Update</router-link
              >
              <router-link
                :to="{ name: 'delete', params: { id: usuario._id['$oid'] } }"
                class="btn btn-danger"
                >Delete</router-link
              >
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data () {
      return {
        usuarios: []
      }
    },
  
    created: function () {
      this.fetchUsuarioData()
    },
  
    methods: {
      fetchUsuarioData: function () {
        this.$http.get('http://localhost:5000/index').then(
          (response) => {
            this.usuarios = response.body
          },
          (response) => {}
        )
      }
    }
  }
  </script>
  