<template>
  <div id="editar-container">
    <div id="container">
      <h1>Editar Perfil</h1>

      <form @submit.prevent="atualizarPerfil" class="editar-form">
        <div class="form-group">
          <label>Nome de Usuário:</label>
          <input type="text" v-model="usuario.username" required />
        </div>

        <div class="form-group">
          <label>Email:</label>
          <input type="email" v-model="usuario.email" required />
        </div>

        <div class="form-group">
          <label>
            <input type="checkbox" v-model="trocarSenha" />
            Trocar senha
          </label>
        </div>

        <div class="form-group" v-if="trocarSenha">
          <label>Nova Senha:</label>
          <input type="password" v-model="novaSenha" />
        </div>

        <div class="form-group" v-if="trocarSenha">
          <label>Confirmar Nova Senha:</label>
          <input type="password" v-model="confirmarSenha" />
        </div>

        <div class="form-group">
          <label>Foto de perfil:</label>
          <input type="file" accept="image/*" @change="processarImagem" />
        </div>

        <button type="submit" class="btn btn-primary">Salvar Alterações</button>
      </form>

      <div class="voltar">
        <router-link :to="{ name: 'perfil' }">← Voltar ao perfil</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import '../assets/editarprofile.css';
export default {
  data() {
    return {
      usuario: {
        id: '',
        username: '',
        email: '',
        password: '',
        foto: ''
      },
      novaSenha: '',
      confirmarSenha: '',
      trocarSenha: false
    };
  },
  created() {
    const username = localStorage.getItem('username');
    if (!username) {
      alert("Você precisa estar logado.");
      this.$router.push({ name: 'login' });
      return;
    }

    this.$http.get('http://localhost:5000/listusers').then((res) => {
      const user = res.body.find(u => u.username === username);
      if (user) {
        this.usuario.id = user._id.$oid;
        this.usuario.username = user.username;
        this.usuario.email = user.email;
        this.usuario.foto = user.foto || '';
      }
    });
  },
  methods: {
    processarImagem(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          this.usuario.foto = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    },
    atualizarPerfil() {
      if (this.trocarSenha) {
        if (!this.novaSenha || this.novaSenha !== this.confirmarSenha) {
          alert("As senhas não coincidem ou estão vazias.");
          return;
        }
        this.usuario.password = this.novaSenha;
      } else {
        this.usuario.password = ''; // será ignorado pelo backend
      }

      this.$http.post('http://localhost:5000/updateuser', this.usuario, {
        headers: { 'Content-Type': 'application/json' }
      }).then(
        (res) => {
          alert(res.body.mensagem);
          localStorage.setItem('username', this.usuario.username);
          this.$router.push({ name: 'perfil' });
        },
        (err) => {
          alert((err.body && err.body.mensagem) || 'Erro ao atualizar perfil');
        }
      );
    }
  }
};
</script>