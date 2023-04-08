import {createRouter, createWebHistory} from "vue-router";
import MainLayout from "@/components/MainLayout.vue";
import ServerList from "@/components/server/ServerList.vue";
import UserList from "@/components/user/UserList.vue";
import DashBoard from "@/components/dashboard/DashBoard.vue";
import TaskPage from "@/components/task/TaskPage.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: MainLayout
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: DashBoard
    },
    {
        path: '/server/list/',
        name: 'ServerList',
        component: ServerList
    },
    {
        path: '/user/list',
        name: 'UserList',
        component: UserList
    },
    {
        path: '/task',
        name: 'Task',
        component: TaskPage
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;