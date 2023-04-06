<template>
    <a-row>
        <a-col :span="8">
            <a-button type="primary">添加服务器</a-button>
        </a-col>
        <a-col :span="8">col-8</a-col>
        <a-col :span="8">col-8</a-col>
    </a-row>
    <a-divider type="horizontal"/>
    <a-table :columns="columns" :data-source="data">
        <template #headerCell="{ column }">
            <span>{{ column.title }}</span>
        </template>

        <template #bodyCell="{ column, record }">
            <template v-if="column.key === 'action'">
                <span>
                    <a-space size="middle">
                    <GrafanaApi/>
                    <EditServer/>
                    <a-button type="ghost">远程连接</a-button>
                    <a-button type="ghost">删除</a-button>
                </a-space>



                </span>
            </template>
            <template v-else-if="column.key === 'status_display'">
                <span>
                    <a-tag :color="record.status === 1 ? 'green' : 'red'">
                        {{ record.status === 1 ? '在线' : '离线' }}
                    </a-tag>
                </span>
            </template>
            <template v-else>
                <span>{{ record[column.key] }}</span>
            </template>
        </template>
    </a-table>
</template>
<script>
import {defineComponent} from 'vue';
import axios from "axios";
import GrafanaApi from "@/components/server/GrafanaApi.vue";
import EditServer from "@/components/server/EditServer.vue";

export default defineComponent({
    components: {EditServer, GrafanaApi},
    data() {
        return {
            data: [],
            columns: [
                {
                    title: 'IP地址',
                    dataIndex: 'ip_address',
                    key: 'ip_address',
                }, {
                    title: '端口',
                    dataIndex: 'port',
                    key: 'port',
                }, {
                    title: '用户名',
                    dataIndex: 'username',
                    key: 'username',
                }, {
                    title: '密码',
                    key: 'password',
                    dataIndex: 'password',
                }, {
                    title: '状态',
                    key: 'status_display',
                    dataIndex: 'status_display',
                }, {
                    title: '所有者',
                    key: 'owner',
                    dataIndex: 'owner',
                }, {
                    title: '操作',
                    key: 'action',
                }
            ]
        }
    },
    created() {
        axios
            .get('/api/server')
            .then(res => (this.data = res.data))
    }
})
</script>
