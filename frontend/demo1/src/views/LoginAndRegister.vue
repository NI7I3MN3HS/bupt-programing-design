<template>
    <div class="body">

        <div class="func">
            <n-tabs class="card-tabs" default-value="signin" size="large" animated style="margin: 0 -4px"
                pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;">
                <n-tab-pane name="signin" tab="登录">
                    <n-form>
                        <n-form-item-row label="用户名">
                            <n-input />
                        </n-form-item-row>
                        <n-form-item-row label="密码">
                            <n-input />
                        </n-form-item-row>
                    </n-form>
                    <n-button type="primary" block secondary strong>
                        登录
                    </n-button>
                </n-tab-pane>
                <n-tab-pane name="signup" tab="注册">
                    <n-form>
                        <n-form-item-row label="用户名">
                            <n-input />
                        </n-form-item-row>
                        <n-form-item-row label="密码">
                            <n-input />
                        </n-form-item-row>
                        <n-form-item-row label="重复密码">
                            <n-input />
                        </n-form-item-row>
                    </n-form>
                    <n-button type="primary" block secondary strong>
                        注册
                    </n-button>
                </n-tab-pane>
            </n-tabs>
        </div>
    </div>
</template>

<script setup>

</script>

<style lang="less" scoped>
.body {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: #f0f2f5;
}
</style>