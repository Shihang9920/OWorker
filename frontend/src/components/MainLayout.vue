<template>
    <a-layout style="min-height: 100vh">
        <a-layout-sider v-model:collapsed="collapsed" collapsible>
            <div class="title">VUE-ANTD</div>
            <a-menu v-model:selectedKeys="selectedKeys" theme="dark" mode="inline">
                <a-menu-item key="1" @click="goToDashboard">
                    <pie-chart-outlined/>
                    <span>仪表盘</span>
                </a-menu-item>
                <a-menu-item key="2" @click="goToServerList">
                    <desktop-outlined/>
                    <span>服务器管理</span>
                </a-menu-item>
                <a-menu-item key="3" @click="goToTask">
                    <FileDoneOutlined />
                    <span>任务管理</span>
                </a-menu-item>
                <a-sub-menu key="sub1">
                    <template #title>
            <span>
              <user-outlined/>
              <span>用户</span>
            </span>
                    </template>
                    <a-menu-item key="3">Tom</a-menu-item>
                    <a-menu-item key="4">Bill</a-menu-item>
                    <a-menu-item key="5">Alex</a-menu-item>
                </a-sub-menu>
                <a-sub-menu key="sub2">
                    <template #title>
            <span>
              <team-outlined/>
              <span>Team</span>
            </span>
                    </template>
                    <a-menu-item key="6">Team 1</a-menu-item>
                    <a-menu-item key="8">Team 2</a-menu-item>
                </a-sub-menu>
                <a-menu-item key="9">
                    <file-outlined/>
                    <span>File</span>
                </a-menu-item>
            </a-menu>
        </a-layout-sider>
        <a-layout>
            <a-layout-header style="background: #fff; padding: 0"/>
            <a-layout-content style="margin: 0 16px">

                <a-breadcrumb style="margin: 16px 0">
                    <a-breadcrumb-item>面包屑</a-breadcrumb-item>
                    <a-breadcrumb-item>导航</a-breadcrumb-item>
                </a-breadcrumb>

                <div :style="{ padding: '24px', background: '#fff', minHeight: '360px' }">
                    <router-view/>

                </div>
            </a-layout-content>
            <a-layout-footer style="text-align: center">
                Ant Design ©2018 Created by Ant UED
            </a-layout-footer>
        </a-layout>
    </a-layout>
</template>
<script>
import {PieChartOutlined, DesktopOutlined, UserOutlined, TeamOutlined, FileOutlined,FileDoneOutlined} from '@ant-design/icons-vue';
import {defineComponent, ref} from 'vue';
import router from "@/router";

export default defineComponent({
    components: {
        PieChartOutlined,
        DesktopOutlined,
        UserOutlined,
        TeamOutlined,
        FileOutlined,
        FileDoneOutlined,
    },
    data() {
        return {
            collapsed: ref(false),
            selectedKeys: ref(['1']),
        };
    },
    methods: {
        goToServerList() {
            router.push('/server/list/')
        },
        goToDashboard() {
            router.push('/dashboard')
        },
        goToTask(){
            router.push('/task')
        }
    }
});
</script>
<style>
#components-layout-demo-side .logo {
    height: 32px;
    margin: 16px;
    background: rgba(255, 255, 255, 0.3);
}

.site-layout .site-layout-background {
    background: #fff;
}

.title {
    font-size: 25px;
    color: white;
    font-family: "hooge 05_53", serif;
    text-align: center;
}

[data-theme='dark'] .site-layout .site-layout-background {
    background: #141414;
}
</style>