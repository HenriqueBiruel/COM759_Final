# 📚 COM759 - Sistema de Gestão de Mídias

🎓 FACAMP – Programação Avançada

---

## ✅ Funcionalidades

- Cadastro de usuários com autenticação (login e senha)
- Login com verificação de credenciais
- Cada usuário vê apenas suas mídias cadastradas
- Operações completas de CRUD em mídias (filmes e séries)
- Edição e exclusão de mídias
- Edição restrita (usuário só pode alterar a avaliação)
- Autocomplete com dados reais da TMDb
- Preenchimento automático de dados da mídia (título, tipo, gênero, ano, descrição)
- Exibição de pôster da mídia na listagem (via URL da TMDb)
- Página de perfil com visualização de dados
- Edição de perfil (nome, email e senha)
- Upload e exibição de imagem de perfil (base64)
- Interface moderna com CSS customizado
- Layout responsivo e intuitivo

---

## 🧰 Tecnologias utilizadas

### 🔹 Frontend (Vue.js)
- Vue 2 com Vue Router
- Axios para requisições HTTP
- HTML5 + CSS3 personalizados

### 🔹 Backend (Flask)
- Flask + Flask-CORS
- PyMongo (integração com MongoDB Atlas)
- Werkzeug (criptografia de senha)
- python-dotenv (variáveis de ambiente)

### 🔹 Banco de Dados
- MongoDB Atlas (NoSQL)
- Collections: `usuario`, `midias`

---

## 📂 Organização do projeto

```
COM759_Final/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env              # Contém TMDB_API_KEY (ignorado pelo Git)
│   └── ... (outras rotas e helpers)
├── frontend/
│   ├── components/
│   │   ├── Login.vue
│   │   ├── Create.vue
│   │   ├── List.vue
│   │   ├── Update.vue
│   │   ├── Profile.vue
│   │   └── EditarPerfil.vue
│   ├── assets/
│   │   └── global.css
│   │   └── list.css
│   │   └── create.css
│   ├── router/
│   │   └── index.js
│   └── ...
```

---

## 📌 Observações

- O projeto foi desenvolvido com base nos critérios exigidos pela disciplina.
- As imagens de perfil são armazenadas como base64 diretamente no MongoDB.
- Os pôsteres das mídias são exibidos diretamente via URL da API da TMDb.
- A API Key da TMDb é protegida por `.env` e **não é enviada para o GitHub**.
- O sistema possui proteção básica para rotas (verificação via `localStorage`).

---

## 👨‍💻 Autor

**Henrique Biruel**
🔗 [github.com/HenriqueBiruel](https://github.com/HenriqueBiruel)