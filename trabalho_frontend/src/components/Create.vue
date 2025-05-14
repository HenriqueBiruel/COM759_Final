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
                  required
                />
              </div>

              <div class="tipo">
                <select v-model="midia.tipo" required>
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
                  required
                />
              </div>

              <div class="ano">
                <input
                  type="text"
                  placeholder="Ano"
                  v-model="midia.ano"
                  @input="applyYearMask"
                  required
                />
              </div>

              <div class="descricao">
                <textarea
                  placeholder="Descrição"
                  v-model="midia.descricao"
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

              <div class="entrar">
                <input type="submit" id="login-btn" value="Cadastrar" />
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
        avaliacao: ''
      }
    };
  },
  methods: {
    addMidia() {
      this.$http
        .post('http://localhost:5000/create', this.midia, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then(
          (response) => {
            this.midia = {};
            alert(response.body.mensagem);
            this.$router.push({ name: 'list' });
          },
          (error) => {
            alert((error.body && error.body.mensagem) || 'Erro ao cadastrar mídia');
          }
        );
    },
    applyYearMask(event) {
      let value = event.target.value.replace(/\D/g, ''); // Remove caracteres não numéricos
      if (value.length > 4) value = value.slice(0, 4); // Limita a 4 dígitos
      if (parseInt(value) > 2025) value = '2025'; // Limita o valor máximo a 2025
      event.target.value = value;
      this.midia.ano = value;
    },
    applyRatingMask(event) {
      let value = event.target.value.replace(/[^0-9.]/g, ''); // Remove caracteres não numéricos e não ponto
      if (value.includes('.')) {
        const [integer, decimal] = value.split('.');
        value = `${integer.slice(0, 1)}.${decimal.slice(0, 1)}`; // Limita a 1 casa decimal
      } else {
        value = value.slice(0, 2); // Limita o valor inteiro a 2 dígitos
      }
      if (parseFloat(value) > 10) value = '10'; // Limita o valor máximo a 10
      event.target.value = value;
      this.midia.avaliacao = value;
    }
  }
};
</script>
