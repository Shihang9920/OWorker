<template>
    <a-row>
        <a-col :span="6">
            <add-server/>
        </a-col>
        <a-col :span="6"></a-col>
        <a-col :span="6"></a-col>
        <a-col :span="6">
            <a-input-search
                    v-model:value="value"
                    placeholder="input search text"
                    enter-button
                    @search="onSearch"
            />
        </a-col>
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
                        <a-button danger>删除</a-button>
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
import AddServer from "@/components/server/AddServer.vue";

export default defineComponent({
    components: {AddServer, EditServer, GrafanaApi},
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