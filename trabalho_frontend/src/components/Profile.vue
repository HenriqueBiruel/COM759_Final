<template>
  <div id="perfil-container">
    <div id="container">
      <h1>Perfil do Usuário</h1>

      <div class="foto-perfil" v-if="usuario.foto">
        <img :src="usuario.foto" alt="Foto de perfil" class="foto-img" />
      </div>

      <div class="perfil-info">
        <p><strong>Usuário:</strong> {{ usuario.username }}</p>
        <p><strong>Email:</strong> {{ usuario.email }}</p>
      </div>

      <button @click="irParaEdicao" class="btn btn-primary">Editar Perfil</button>

      <div class="voltar">
        <router-link :to="{ name: 'list' }">← Voltar para a lista</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import '../assets/profile.css';
export default {
  data() {
    return {
      usuario: {
        username: '',
        email: '',
        foto: ''
      }
    };
  },
created() {
  const userId = localStorage.getItem('user_id');
  if (!userId) {
    alert("Você precisa estar logado.");
    this.$router.push({ name: 'login' });
    return;
  }

  this.$http.get(`http://localhost:5000/getuser/${userId}`).then(
    (res) => {
      this.usuario.username = res.body.username;
      this.usuario.email = res.body.email;
      this.usuario.foto = res.body.foto || '';
    },
    () => {
      alert("Erro ao carregar os dados do usuário.");
      this.$router.push({ name: 'login' });
    }
  );
},

  methods: {
    irParaEdicao() {
      this.$router.push({ name: 'editarperfil' });
    }
  }
};
</script>
