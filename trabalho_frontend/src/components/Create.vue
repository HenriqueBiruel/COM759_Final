<template>
    <div id="create-usuario">
      <h1>Create Usuário</h1>
  
      <p>
        <router-link :to="{ name: 'list' }"
          >Voltar para a lista de usuarios</router-link
        >
      </p>
      <form v-on:submit.prevent="addUsuario">
        <div class="form-group">
          <label name="usuario_nome">Nome</label>
          <input
            type="text"
            class="form-control"
            v-model="usuario.nome"
            id="usuario_nome"
            required
          />
        </div>
  
        <div class="form-group">
          <label name="usuario_email">E-mail</label>
          <input
            type="text"
            class="form-control"
            v-model="usuario.email"
            id="usuario_email"
            required
          />
        </div>
  
        <div class="form-group">
          <label name="usuario_idade">Idade</label>
          <input
            type="text"
            class="form-control"
            v-model="usuario.idade"
            id="usuario_idade"
            required
          />
        </div>
  
        <div class="form-group">
          <button class="btn btn-primary">Create</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data () {
      return {
        usuario: {}
      }
    },
    methods: {
      addUsuario: function () {
        // Validation
        var idade = parseFloat(this.usuario.idade)
        if (isNaN(idade)) {
          alert('Idade deve ser um número')
          return false
        } else {
          this.usuario.idade = this.usuario.idade
        }
        this.$http
          .post('http://localhost:5000/create', this.usuario, {
            headers: {
              'Content-Type': 'application/json'
            }
          })
          .then(
            (response) => {
              this.usuario = {}
              alert(response.body['mensagem'])
              this.$router.push('list')
            },
            (response) => {
              alert(response.body['mensagem'])
            }
          )
      }
    }
  }
  </script>
  