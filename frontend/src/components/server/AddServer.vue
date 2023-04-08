<template>
    <div>
        <a-button type="primary" @click="showModal">
            <PlusOutlined/>
            添加
        </a-button>
        <a-modal v-model:visible="visible" title="添加服务器" @ok="handleOk">

            <a-form :label-col="{ span: 4 }"
                    :wrapper-col="{ span: 16 }">
                <a-form-item name="ipaddress" label="服务器IP">
                    <a-input/>
                </a-form-item>
                <a-form-item name="port" label="端口">
                    <a-input-number/>
                </a-form-item>
                <a-form-item name="username" label="用户名">
                    <a-input/>
                </a-form-item>
                <a-form-item name="password" label="密码">
                    <a-input-password/>
                </a-form-item>
            </a-form>

        </a-modal>
    </div>
</template>
<script>
import {defineComponent, ref} from 'vue';
import {PlusOutlined} from '@ant-design/icons-vue';

export default defineComponent({
    components: {PlusOutlined},
    setup() {
        const visible = ref(false);
        const showModal = () => {
            visible.value = true;
        };
        const handleOk = e => {
            console.log(e);
            visible.value = false;
        };
        return {
            visible,
            showModal,
            handleOk,
        };
    },
});
</script>