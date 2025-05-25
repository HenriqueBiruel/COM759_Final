import Vue from 'vue'
import Router from 'vue-router'
import VueResource from 'vue-resource'
import Create from '../components/Create.vue'
import Update from '../components/Update.vue'
import List from '../components/List.vue'
import Delete from '../components/Delete.vue'
import Cadastro from '@/components/Cadastro.vue'
import Login from '@/components/Login.vue'
import Profile from '@/components/Profile.vue'
import EditarPerfil from '../components/EditarPerfil.vue'

Vue.use(Router)
Vue.use(VueResource)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/create',
      name: 'create',
      component: Create
    },
    {
      path: '/update',
      name: 'update',
      component: Update
    },
    {
      path: '/list',
      name: 'list',
      component: List
    },
    {
      path: '/delete',
      name: 'delete',
      component: Delete
    },
    {
      path: '/cadastro',
      name: 'cadastro',
      component: Cadastro
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/perfil',
      name: 'perfil',
      component: Profile
    },
    {
      path: '/editarperfil',
      name: 'editarperfil',
      component: EditarPerfil
    },
    {
      path: '/',
      redirect: '/login' // Rota padrão tela de login
    }
  ]
})
