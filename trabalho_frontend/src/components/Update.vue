<template>
    <div id="update-usuario">
      <h1>Update Usuário</h1>
  
      <p>
        <router-link :to="{ name: 'list' }"
          >Voltar para a lista de usuarios</router-link
        >
      </p>
      <form v-on:submit.prevent="updateUsuario">
        <div class="form-group">
          <label name="usuario_id">ID</label>
          <input
            type="text"
            class="form-control"
            disabled
            v-model="usuario.id"
            id="usuario_id"
          />
        </div>
  
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
          <button class="btn btn-primary">Update</button>
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
    created: function () {
      this.getUsuarioData()
    },
    methods: {
      getUsuarioData: function () {
        this.$http.get('http://localhost:5000/getid/' + this.$route.params.id).then(
          (response) => {
            this.usuario.id = this.$route.params.id
            this.usuario.nome = response.body['nome']
            this.usuario.email = response.body['email']
            this.usuario.idade = response.body['idade']
            this.$forceUpdate()
          },
          (response) => {}
        )
      },
      updateUsuario: function () {
        // Validation
        var idade = parseFloat(this.usuario.idade)
        if (isNaN(idade)) {
          alert('Idade deve ser um número')
          return false
        } else {
          this.usuario.idade = this.usuario.idade
        }
        this.$http
          .post('http://localhost:5000/update', this.usuario, {
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
  