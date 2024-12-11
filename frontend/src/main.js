import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import App from './App.vue'
import FoodItems from './components/FoodItems.vue'
import './assets/styles.css';


import CompaniesPage from "./components/CompaniesPage.vue";
import EmployeeFormPage from "./components/EmployeeFormPage.vue";
import EmployeePage from "./components/EmployeePage.vue";
import LoginPage from "./components/LoginPage.vue";
import DepartmentsPage  from './components/DepartmentsPage.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: "/", component: LoginPage, name: "LoginPage" },
        { path: "/companies", component: CompaniesPage, name: "CompaniesPage" },
        
        { path: "/departments", component: DepartmentsPage, name: "DepartmentsPage" },
        { path: "/employees/new", component: EmployeeFormPage, name: "EmployeeFormPage" },
        { path: "/employees", component: EmployeePage, name: "EmployeePage" },
        { path: '/food', component: FoodItems },
    ]
});

const app = createApp(App)

app.use(router);
app.component('food-items', FoodItems);

app.mount('#app')