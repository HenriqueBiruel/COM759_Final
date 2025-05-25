# Sistema de Gestão de Mídias – COM759

## 1. Cadastro e Login de Usuários

* Usuários podem se cadastrar com **nome**, **email** e **senha**.
* As **senhas são criptografadas** no backend.
* Após o login, um `user_id` é armazenado no **localStorage** para identificar o usuário nas ações futuras.

## 2. CRUD de Mídias

Cada usuário vê apenas suas próprias mídias. É possível:

* **Cadastrar** uma nova mídia.
* **Listar** as mídias cadastradas.
* **Editar** apenas a **avaliação** da mídia.
* **Excluir** uma mídia.

## 3. Integração com a API da TMDb

* Ao digitar um título, o sistema sugere automaticamente filmes ou séries reais.
* Após selecionar, o sistema preenche automaticamente os seguintes campos:

  * **Título**
  * **Tipo**
  * **Gênero**
  * **Ano**
  * **Descrição**
  * **Imagem de pôster** (usada apenas na listagem)

## 4. Perfil de Usuário

* O usuário pode editar seus dados: **nome**, **email** e **senha**.
* A senha só é atualizada se uma nova for informada.

## 5. Controle de Acesso

* Cada usuário acessa **apenas seus próprios dados**.
* O sistema realiza checagens de autenticação via **localStorage**.

---

## Como Rodar o Projeto

### 1. Clone o Repositório

```bash
git clone https://github.com/HenriqueBiruel/COM759_Final.git
cd COM759_Final
```

### 2. Configurar o Backend

```bash
cd trabalho_backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Crie o arquivo `.env` e adicione a chave da TMDb:

```env
TMDB_API_KEY=sua_chave_aqui
```

### 3. Configurar e Rodar o Frontend (Vue.js)

```bash
cd ../trabalho_frontend
npm install
npm run dev
```

---

**Autor:** Henrique Biruel
[github.com/HenriqueBiruel](https://github.com/HenriqueBiruel)
