<template>
    <div class ="background">
        <div class="user">
           <n-card title="昵称">
            <template #cover>
                <img src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg">
            </template>
            自我介绍
           </n-card>
        </div>
    </div>
</template>

<script setup>

</script>

<style lang="less" scoped>
.background{
    position: absolute;
    width: 100%;
    background-color: rgb(216, 214, 218);
    height: 1500px;
  .user{
    max-width: 300px;
}
}
</style>