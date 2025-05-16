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
    const username = localStorage.getItem('username');
    if (!username) {
      alert("Você precisa estar logado.");
      this.$router.push({ name: 'login' });
      return;
    }

    this.$http.get(`http://localhost:5000/listusers`).then((res) => {
      const user = res.body.find(u => u.username === username);
      if (user) {
        this.usuario.username = user.username;
        this.usuario.email = user.email;
        this.usuario.foto = user.foto || '';
      }
    });
  },
  methods: {
    irParaEdicao() {
      this.$router.push({ name: 'editarperfil' });
    }
  }
};
</script>
