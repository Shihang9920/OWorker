<template>
    <a-button type="primary" @click="showDrawer">监控</a-button>
    <a-drawer
            width="80%"
            title="仪表盘"
            placement="right"
            :closable="false"
            v-model:visible="visible"
            :after-visible-change="afterVisibleChange"
    >

        <div>
            <div v-if="panelUrl">
                <iframe :src="panelUrl" width="1000" height="500"></iframe>
            </div>
            <div v-else>
                Loading...
            </div>
        </div>


    </a-drawer>
</template>
<script>
import {defineComponent, ref} from 'vue';
import axios from "axios";

export default defineComponent({
    setup() {
        const visible = ref(false);
        const afterVisibleChange = bool => {
            console.log('visible', bool);
        };
        const showDrawer = () => {
            visible.value = true;
        };

        return {
            visible,
            afterVisibleChange,
            showDrawer,

            panelUrl: null,
            panelUid: '6ailAtY4z',
            apiBaseUrl: 'http://192.168.31.150:3000/',
            apiKey: 'eyJrIjoiWGdRTHVJTTJNcVhZcUE4Nzk0ZjQ5cWR6NnBkaFFIMEIiLCJuIjoiVGVzdCIsImlkIjoxfQ=='
        };

    },
    created() {
        const params = {width: 1000, height: 500}
        const headers = {Authorization: `Bearer ${this.apiKey}`}
        axios.get(`${this.apiBaseUrl}/api/dashboards/uid/${this.panelUid}`, {params, headers})
            .then(response => {
                this.panelUrl = response.data.dashboard.url
            })
            .catch(error => {
                console.error(error)
            })
    }
});
</script>