import { createWebHistory, createRouter } from 'vue-router'
import Login from '@/components/Login.vue'
import Index from '@/components/Index.vue'
import UserList from '@/components/userList.vue'
import Register from '@/components/Register.vue'
import Dashboard from '@/components/DashBoard.vue'


const routes = [{
        path: '/',
        name: 'Index',
        component: Index
    }, {
        path: '/login',
        name: 'Login',
        component: Login
    }, {
        path: '/userList',
        name: 'UserList',
        component: UserList
    }, {
        path: '/login/register',
        name: 'Register',
        component: Register
    }, {
        path: '/dashboard',
        name: 'dashboard',
        component: Dashboard
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
