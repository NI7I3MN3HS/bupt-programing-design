<template>
    <div class="settingview">
        <div class="pagehead">
            <div class="pagetitle">
                <i class="icon">
                    <n-icon size="40" :component="SettingsOutline" />
                </i>
                <span class="vm">账号设置</span>
            </div>
        </div>
        <div class="pagemain">
            <nav class="navigation">
                <ul class="swiper">
                    <li class="slide">
                        <router-link to="/profile/edit1">
                            <span class="route">
                                个人资料
                            </span>
                        </router-link>
                    </li>
                    <li class="slide">
                        <router-link to="/profile/edit2">
                            <span class="route exact">
                                账号信息
                            </span>
                        </router-link>
                    </li>
                </ul>
            </nav>
            <div class="pageview">
                <div class="pageview_view">
                    <div class="_head">账号信息</div>
                    <div class="_main">
                        <div class="_form">
                            <label class="_wrapper">
                                <span class="_intro">账号邮箱</span>
                                <div class="_put">
                                    <!-- 后端？（学一下 -->
                                    <input class="_input" placeholder="原邮箱">
                                    <n-button round class="_button1">点击修改</n-button>
                                </div>
                            </label>
                            <label class="_item">
                                <span class="_intro">账号密码</span>
                                <div class="_button2">
                                    <router-link to="/profile/edit3">
                                        <n-button type="tertiary">修改密码</n-button>
                                    </router-link>
                                </div>
                            </label>
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
        display: flex; 
        max-width: 948px;
        margin: auto; 
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
                    a {
                        text-decoration: none;
                    }
                    .router-link-active {
                        text-decoration: none;    
                    }
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
                    ._form {
                        padding: 24px 0 0 0;
                        position: absolute;
                        display: flex;
                        flex-direction: column;
                        flex: 1;
                        ._wrapper {
                            min-height: calc(15vh);
                            display: flex;
                            flex-direction: column;
                            ._intro {
                                display: flex;
                                width: 650px;
                                font-weight: 500;
                                color: #655e5e;
                                margin-bottom: 8px;
                            }
                            ._put {
                                display: flex;
                                ._input {
                                    display: flex;
                                    width: 540px;
                                    padding: 10px 12px;
                                    background: #f7f7f8;
                                    border: none;
                                    outline-style: none;
                                    font-size: 16px;
                                    line-height: 22px;
                                    margin-right: 24px;
                                }
                                ._button1 {
                                    display: flex;
                                    width: 100px;
                                }
                            }
                        }
                        ._item {
                            min-height: calc(15vh);
                            ._intro {
                                display: flex;
                                width: 650px;
                                font-weight: 500;
                                color: #655e5e;
                                margin-bottom: 8px;
                            }
                            ._button2 {
                                display: flex;
                                width: 250px;
                                left: 10px;
                            }
                        }
                    }
                }
            }
        }
    }
}</style>