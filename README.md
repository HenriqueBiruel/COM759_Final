Sistema de Gestão de Mídias – COM759

1. **Cadastro e login de usuários**

* Usuários podem se cadastrar com nome, email e senha.
* As senhas são criptografadas no backend.
* Após o login, um user_id é armazenado no localStorage para identificar o usuário nas ações futuras.

2. **CRUD de mídias**

* Cada usuário vê apenas suas mídias.
* É possível:

  * Cadastrar uma nova mídia.
  * Listar as mídias cadastradas.
  * Editar apenas a avaliação da mídia.
  * Excluir uma mídia.

3. **Integração com a API da TMDb**

* Ao digitar um título, o sistema sugere automaticamente filmes ou séries reais.
* Após selecionar, o sistema preenche automaticamente:

  * Título
  * Tipo
  * Gênero
  * Ano
  * Descrição
  * Imagem de pôster (usada apenas na listagem)

**Perfil de usuário**
O usuário pode editar seus dados: nome, email e senha.
A senha é atualizada somente se informada.

**Controle de acesso**

Cada usuário acessa apenas seus dados.
O sistema faz checagens de autenticação via localStorage.


**Como rodar o projeto**

**Clone o repositório**

git clone https://github.com/HenriqueBiruel/COM759_Final.git
cd COM759_Final

**Configurar o backend**

cd trabalho_backend
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

Crie o arquivo `.env`, dentro desse arquivo adicione a chave da TMDb:
(O arquivo deve ficar dessa maneira, troque sua_chave_aqui pelo sua chave)
TMDB_API_KEY=sua_chave_aqui

Configurar e rodar o frontend (Vue.js)
cd ../trabalho_frontend
npm install
npm run serve

Autor: Henrique Biruel
github.com/HenriqueBiruel (https://github.com/HenriqueBiruel)
