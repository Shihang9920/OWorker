<template>
    <a-row style="text-align: center">
        <a-col :span="6"></a-col>
        <a-col :span="6"></a-col>
        <a-col :span="6"></a-col>
        <a-col :span="6"><avatar-block/></a-col>
    </a-row>
</template>

<script>
import AvatarBlock from "@/components/topbar/AvatarBlock.vue";
export default {
    name: "TopBar",
    components: {AvatarBlock}
}
</script>

<style scoped>

</style>