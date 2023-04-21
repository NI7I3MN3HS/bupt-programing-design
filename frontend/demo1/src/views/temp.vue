<n-card>
    <n-tabs
      class="card-tabs"
      default-value="signin"
      size="large"
      animated
      style="margin: 0 -4px"
      pane-style="padding-left: 4px; padding-right: 4px; box-sizing: border-box;"
    >
      <n-tab-pane name="signin" tab="登录">
        <n-form :model="LoginValue">
          <n-form-item-row label="用户名">
            <n-input v-model:value="LoginValue.username" />
          </n-form-item-row>
          <n-form-item-row label="密码">
            <n-input v-model:value="LoginValue.password" />
          </n-form-item-row>
        </n-form>
        <n-button type="primary" block secondary strong @click="clicklogin">
          登录
        </n-button>
      </n-tab-pane>
      <n-tab-pane name="signup" tab="注册">
        <n-form :model="Email">
          <n-form-item-row label="邮箱">
            <n-input v-model:value="Email.email" />
          </n-form-item-row>
        </n-form>
        <n-form :model="RegisterValue">
          <n-button
            type="primary"
            block
            secondary
            strong
            @click="clicksendcode"
          >
            发送验证码
          </n-button>
          <n-form-item-row label="验证码">
            <n-input v-model:value="RegisterValue.Code.code" />
          </n-form-item-row>
          <n-form-item-row label="用户名">
            <n-input v-model:value="RegisterValue.user.username" />
          </n-form-item-row>
          <n-form-item-row label="密码">
            <n-input v-model:value="RegisterValue.user.password" />
          </n-form-item-row>
        </n-form>
        <n-button
          type="primary"
          block
          secondary
          strong
          @click="clickregister"
        >
          注册
        </n-button>
      </n-tab-pane>
    </n-tabs>
  </n-card>
