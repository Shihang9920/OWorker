<template>
    <a-row>
        <a-col :span="8">
            <a-button type="primary">新建任务</a-button>
        </a-col>
        <a-col :span="8">col-8</a-col>
        <a-col :span="8">col-8</a-col>
    </a-row>
    <a-divider type="horizontal"/>
    <a-row :gutter="[16,16]">
        <a-col :span="6">
            <a-card title="Default size card" style="width: 300px">
                <template #extra><a href="#">more</a></template>
                <p>card content</p>
                <p>card content</p>
                <p>card content</p>
            </a-card>
        </a-col>
        <a-col :span="6">
            <a-card title="Default size card" style="width: 300px">
                <template #extra><a href="#">more</a></template>
                <p>card content</p>
                <p>card content</p>
                <p>card content</p>
            </a-card>
        </a-col>
        <a-col :span="6">
            <a-card title="Default size card" style="width: 300px">
                <template #extra><a href="#">more</a></template>
                <p>card content</p>
                <p>card content</p>
                <p>card content</p>
            </a-card>
        </a-col>
        <a-col :span="6">
            <a-card title="Default size card" style="width: 300px">
                <template #extra><a href="#">more</a></template>
                <p>card content</p>
                <p>card content</p>
                <p>card content</p>
            </a-card>
        </a-col>
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