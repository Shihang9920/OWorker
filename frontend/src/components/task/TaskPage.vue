<template>
    <a-row>
        <a-col :span="8"><button>新建任务</button></a-col>
        <a-col :span="8">col-8</a-col>
        <a-col :span="8">col-8</a-col>
    </a-row>
    <a-divider type="horizontal"/>
    <a-row :gutter="[16,16]">
        <a-col :span="6">任务1</a-col>
        <a-col :span="6">任务2</a-col>
        <a-col :span="6">任务3</a-col>
        <a-col :span="6">任务4</a-col>
    </a-row>

    <a-row :gutter="[16,16]">
        <a-col :span="6">任务5</a-col>
        <a-col :span="6">任务6</a-col>
        <a-col :span="6">任务7</a-col>
        <a-col :span="6">任务8</a-col>
    </a-row>
</template>

<script>
export default {
    name: "TaskPage"
}
</script>

<style scoped>

</style>