
## 📚 COM759 - Sistema de Gestão de Mídias

### 🎓 FACAMP – Programação Avançada


## ✅ Funcionalidades

* Cadastro de usuários com autenticação (login e senha)
* Login com verificação de credenciais
* Cada usuário vê apenas suas mídias cadastradas
* Operações completas de CRUD em mídias (filmes e séries)
* Edição e exclusão de mídias
* Página de perfil com visualização de dados
* Edição de perfil (nome, email e senha)
* Upload e exibição de imagem de perfil (base64)
* Interface moderna com CSS customizado
* Layout responsivo e intuitivo

---

## 🧰 Tecnologias utilizadas

Frontend (Vue.js)

Vue 2 com Vue Router
Axios para requisições HTTP
HTML5 + CSS3 personalizados

Backend (Flask)

Flask + Flask-CORS
PyMongo (integração com MongoDB Atlas)
Werkzeug (criptografia de senha)

Banco de Dados

MongoDB Atlas (NoSQL)
Collections: `usuario`, `midias`



## 📂 Organização do projeto

```
COM759_Final/
├── backend/
│   └── app.py
│   └── requirements.txt
│   └── ... (outras rotas e helpers)
├── frontend/
│   ├── components/
│   │   └── Login.vue
│   │   └── Create.vue
│   │   └── List.vue
│   │   └── Profile.vue
│   │   └── EditarPerfil.vue
│   ├── router/
│   │   └── index.js
│   └── ...
```

📌 Observações

O projeto foi desenvolvido com base nos critérios exigidos pela disciplina.
As imagens de perfil são armazenadas como base64 diretamente no MongoDB.
O sistema possui proteção básica para rotas (verificação via localStorage).

👨‍💻 Autor

Henrique Biruel
[github.com/HenriqueBiruel](https://github.com/HenriqueBiruel)
