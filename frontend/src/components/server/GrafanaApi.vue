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
        <h1>仪表盘</h1>
    </a-drawer>
</template>
<script>
import {defineComponent, ref} from 'vue';

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
        };
    },
});
</script>