<template>
    <div class="background">

        <div class="user">

            <!-- <div class="img">
                <img
            src="http://www.runoob.com/wp-content/uploads/2016/04/trolltunga.jpg" 
            alt="Norway" width="100" height="100"
            >
            </div>

            <div class="edit">
                <n-button strong secondary type="tertiary">
                编辑
            </n-button>
            </div> -->

            <div class="user1">

            <el-row>
                <el-col>
    
                <el-card :body-style="{ padding: '0px' }">
                    
                    <img
                    src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                    class="image"/>
                    
                    <div style="padding: 14px">
                        <span>昵称</span>

                        <div class="bottom">

                            <time class="time">{{ currentDate }}</time>
                            <!-- <el-button text class="button">编辑</el-button> -->

                        </div>

                        <div class="edit">
                            <n-button strong secondary type="tertiary">
                                编辑个人资料
                            </n-button>
                        </div> 

                    </div>
                </el-card>
                </el-col>
            </el-row>

            </div>



        </div>

        <div class="relate">
            <div class="relate1">

            <n-card content-style="padding: 0;">
                <n-tabs
                type="line"
                size="large"
                :tabs-padding="20"
                pane-style="padding: 20px;">
                <n-tab-pane name="发帖">
                    发帖
                </n-tab-pane>
                <n-tab-pane name="评论">
                    评论
                </n-tab-pane>
                </n-tabs>
            </n-card>
            </div>

            <n-pagination v-model:page="page" :page-count="20" />

        </div>

        <!-- <n-pagination v-model:page="page" :page-count="20" /> -->

    </div>
</template>

<script setup>

import { ref } from 'vue'

const currentDate = ref(new Date())

</script>

<style lang="less" scoped>
.background {
    position: absolute;
    width: 100%;
    background-color: rgb(233, 232, 235);
    min-height: calc(100vh
     );

    .user {
        position: absolute;
        width: 22%;
        background-color: rgb(255, 255, 255);
        height: 55%;
        left: 15%;
        top: 5%;
        .img{
            left: 5%;
            top: 10%;
        }
        // .edit{
        //     left: 5%;
        //     top: 20%;
        // }

        .user1{
            left: 10%;
            top: 10%;
            width: 70%;


            // .image{
            // left: 5%;
            // top: 10%;
            // width: 20%;
            // }    
        .time {
            font-size: 12px;
            color: #999
        }
        .bottom {
            margin-top: 13px;
            line-height: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        // .button {
        //     padding: 0;
        //     min-height: auto;
        // }
        .image {
            width: 100%;
            display: block;
        }
        // .edit{
        //     left: 5%;
        //     top: 80%;
        // }


        }

    }
    .relate{
        position: absolute;
        width: 46%;
        background-color: rgb(255, 255, 255);
        height: 90%;
        right: 15%;
        top: 5%;
        .relate1{
            left: 5%;
            top: 5%;
            width: 90%;
            // height: 200px;  记得改
        }
    }

    // 换页
    .n-pagination{
        justify-content: center;
        align-items: center;
        // width: 40%;
        // background-color: rgb(255, 255, 255);
        height: 50px;
        // left: 30%;
        top: 75%;
    }
}
</style>