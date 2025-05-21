<template>
  <body>
    <div id="create-container">
      <form @submit.prevent="addMidia">
        <div id="container">
          <div id="titulo">
            <h1>Gestão de Filmes e Séries</h1>
          </div>

          <div class="create-form">
            <h2>Cadastrar Filmes e Séries</h2>

            <div class="create-caixa">
              <div class="titulo">
                <input
                  type="text"
                  placeholder="Título"
                  v-model="midia.titulo"
                  @input="buscarSugestoes"
                  :readonly="bloquearCampos"
                  required
                />
                <ul v-if="sugestoes.length" class="autocomplete">
                  <li v-for="s in sugestoes" :key="s.titulo" @click="selecionarMidia(s)">
                    {{ s.titulo }} ({{ s.tipo }})
                  </li>
                </ul>
              </div>

              <div class="tipo">
                <select v-model="midia.tipo" :disabled="bloquearCampos" required>
                  <option value="" disabled selected>Selecione o tipo</option>
                  <option value="Filme">Filme</option>
                  <option value="Série">Série</option>
                </select>
              </div>

              <div class="genero">
                <input
                  type="text"
                  placeholder="Gênero"
                  v-model="midia.genero"
                  :readonly="bloquearCampos"
                  required
                />
              </div>

              <div class="ano">
                <input
                  type="text"
                  placeholder="Ano"
                  v-model="midia.ano"
                  :readonly="bloquearCampos"
                  required
                />
              </div>

              <div class="descricao">
                <textarea
                  placeholder="Descrição"
                  v-model="midia.descricao"
                  :readonly="bloquearCampos"
                  required
                ></textarea>
              </div>

              <div class="avaliacao">
                <input
                  type="text"
                  placeholder="Avaliação (0 a 10)"
                  v-model="midia.avaliacao"
                  @input="applyRatingMask"
                  required
                />
              </div>

              <div class="botoes">
                <input type="submit" id="login-btn" value="Cadastrar" />
                <input type="reset" id="btn-limpar" value="Limpar" @click="limparCampos" />
              </div>
              <div id="cadastro-link">
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
import '../assets/global.css';

export default {
  data() {
    return {
      midia: {
        titulo: '',
        tipo: '',
        genero: '',
        ano: '',
        descricao: '',
        avaliacao: '',
        imagem: ''
      },
      sugestoes: [],
      bloquearCampos: false
    };
  },
created() {
  const userId = localStorage.getItem('user_id');
  if (!userId) {
    alert("Você precisa estar logado para cadastrar uma mídia.");
    this.$router.push({ name: 'login' });
  }
},

  methods: {
    buscarSugestoes() {
      if (this.midia.titulo.length < 2) {
        this.sugestoes = [];
        return;
      }

      this.$http.get(`http://localhost:5000/tmdb?q=${this.midia.titulo}`).then(
        (res) => {
          this.sugestoes = res.body;
        },
        () => {
          this.sugestoes = [];
        }
      );
    },
    selecionarMidia(sugestao) {
      this.midia.titulo = sugestao.titulo;
      this.midia.tipo = sugestao.tipo;
      this.midia.genero = sugestao.genero;
      this.midia.ano = sugestao.ano;
      this.midia.descricao = sugestao.descricao;
      this.midia.imagem = sugestao.imagem || '';
      this.bloquearCampos = true;
      this.sugestoes = [];
    },
    addMidia() {

      const userId = localStorage.getItem('user_id');
      const midiaComUsuario = {
        ...this.midia,
        user_id: userId
      };


      this.$http
        .post('http://localhost:5000/create', midiaComUsuario, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            this.limparCampos();
            alert(response.body.mensagem);
            this.$router.push({ name: 'list' });
          },
          (error) => {
            alert((error.body && error.body.mensagem) || 'Erro ao cadastrar mídia');
          }
        );
    },
    applyRatingMask(event) {
      let value = event.target.value.replace(/[^0-9.]/g, '');
      if (value.includes('.')) {
        const [integer, decimal] = value.split('.');
        value = `${integer.slice(0, 1)}.${decimal.slice(0, 1)}`;
      } else {
        value = value.slice(0, 2);
      }
      if (parseFloat(value) > 10) value = '10';
      event.target.value = value;
      this.midia.avaliacao = value;
    },
    limparCampos() {
      this.midia = {
        titulo: '',
        tipo: '',
        genero: '',
        ano: '',
        descricao: '',
        avaliacao: '',
        imagem: ''
      };
      this.bloquearCampos = false;
      this.sugestoes = [];
    }
  }
};
</script>
