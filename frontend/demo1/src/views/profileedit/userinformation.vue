<template>
    <div class="settingview">
        <div class="pagehead">
            <div class="pagetitle">
                <i class="icon">
                    <n-icon size="40" :component="SettingsOutline" />
                </i>
                <span class="vm">账号设置</span>
                <!-- 高度不太合适 -->
            </div>
        </div>
        <div class="pagemain">
            <nav class="navigation">
                <!-- 点击后的after未实现 -->
                <ul class="swiper">
                    <li class="slide">
                        <span class="route exact">
                            <router-link to="/profile/edit1">
                                <n-button text strong color="#fd281a" size="large" type="primary">
                                个人资料
                                </n-button>
                            </router-link>
                        </span>
                        <!-- <a herf="" class="route exact">个人资料</a> -->
                    </li>
                    <li class="slide">
                        <span class="route">
                            <router-link to="/profile/edit2">
                                <n-button text strong size="large">
                                    账号信息
                                </n-button>
                            </router-link>
                        </span>
                        <!-- <a herf="" class="route">账号信息</a> -->
                    </li>
                </ul>
            </nav>
            <div class="pageview">
                <div class="pageview_view">
                    <div class="_head">个人资料</div>
                    <div class="_main">
                        <div class="_left">
                            <div class="_image">
                                <div class="_img">
                                    <n-avatar :size="100"
                                        src="https://07akioni.oss-cn-beijing.aliyuncs.com/07akioni.jpeg" />
                                </div>
                                <div class="_imgupload">
                                    <n-button text>
                                        <template #icon>
                                            <n-icon size="20" :component="PictureOutlined" />
                                        </template>
                                        上传头像
                                    </n-button>
                                    <!-- <input>后端？ -->
                                </div>
                            </div>
                        </div>
                        <div class="_right">
                            <label class="_item">
                                <span class="_intro">昵称</span>
                                <input class="_input" placeholder="请输入昵称">
                            </label>
                            <label class="_item">
                                <span class="_intro">个人简介</span>
                                <input class="_input" placeholder="请介绍你自己" maxlength="200">
                            </label>
                            <div class="_button">
                                <n-button type="tertiary">确认提交</n-button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { SettingsOutline } from "@vicons/ionicons5";
import { PictureOutlined } from "@vicons/antd";
import { defineComponent } from "vue";

export default defineComponent({
    components: {
        SettingsOutline,
        PictureOutlined
    },
    setup() {
        return {
            SettingsOutline,
            PictureOutlined
        };
    }
});
</script>

<style lang="less" scoped>
.settingview {
    width: 100%;
    min-height: calc(100vh);
    display: block;
    background: #f3f3f4;

    .pagehead {
        margin: 0px 294px;
        padding: 40px 0px;

        .pagetitle {
            font-size: 28px;

            .icon {
                font-size: 48px;
                margin-right: 10px;
            }

            .vm {
                vertical-align: text-top;
            }
        }
    }

    .pagemain {
        min-height: calc(80vh);
        margin: 0px 294px;
        display: flex; // 将容器指定为flex布局
        max-width: 948px;
        margin: auto; //重要？

        .navigation {
            margin-right: 52px;

            .swiper {
                display: flex;
                flex-direction: column;
                list-style: none;
                width: 180px;

                .slide {
                    margin: 0;
                    text-align: left;
                    border-bottom: 1px solid #e5e5e5;

                    .route {
                        font-size: 16px;
                        font-weight: 600;
                        color: #8e8787;
                        display: block;
                        padding: 16px 0;
                    }

                    .exact {
                        position: relative;
                        color: #fd281a;
                    }
                }
            }
        }

        .pageview {
            background: #ffffff;
            // background: #e4c0c0;//调色看位置用
            flex: 1;
            margin-top: 0;
            margin-bottom: 4px;

            .pageview_view {
                ._head {
                    font-size: larger;
                    font-weight: 1000;
                    border-bottom: 1px solid #e5e5e5;
                    padding: 24px 32px;
                }

                ._main {
                    padding: 0 32px;
                    display: flex;
                    align-items: flex-start;
                    min-height: calc(60vh);

                    // background: #ebd0d0;//调色看位置用
                    ._left {
                        position: absolute;
                        left: 40px;
                        margin: 24px 40px 0 0;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;

                        ._image {
                            margin: 0 0 18px 0;
                            display: inline-block;
                            vertical-align: middle;
                            line-height: normal; //没什
                            position: relative; //么用

                            ._imgupload {
                                margin: 5px 0 0 10px;
                            }
                        }
                    }

                    ._right {
                        padding: 24px 0 0 0;
                        position: absolute;
                        left: 180px;
                        display: flex;
                        flex-direction: column;
                        flex: 1;

                        ._item {
                            // width: calc(100%-200px);
                            //在此处宽度值无效
                            min-height: calc(15vh);

                            // background: #e5e5e5;//调色看位置用
                            ._intro {
                                display: flex;
                                width: 490px;
                                font-weight: 500;
                                color: #655e5e;
                                margin-bottom: 8px;
                            }

                            ._input {
                                display: flex;
                                width: 490px;
                                padding: 10px 12px;
                                background: #f7f7f8;
                                border: none;
                                outline-style: none;
                                font-size: 16px;
                                line-height: 22px
                            }

                            //这里括号位置粗心大意>_<耽误好多时间
                            ._button {
                                display: flex;
                                width: 250px;
                            }
                        }
                    }
                }
            }
        }
    }
}
</style>