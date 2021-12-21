有如下代码

```vue
<template>
    <div>
        <el-row>
            <el-col :span='12'>
                <el-card class="box-card">
                    <div slot="header" class="card-header">
                        <span>我是第一个卡片</span>
                    </div>
                    <div class=card-body>
                        <p>11111</p>
                        <p>11111</p>
                        <p>11111</p>
                        <p>11111</p>
                        <p>11111</p>
                    </div>
                </el-card>
            </el-col>
            <el-col :span='12'>
                <el-card class="box-card">
                    <div slot="header" class="card-header">
                        <span>我是第二个卡片</span>
                    </div>
                    <div class=card-body>
                        <p>222222222</p>
                        <p>222222222</p>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<scripts>

</scripts>

<style scoped>

</style>
```

组件中定义了一个栅格，并在并列的一行内放置了两个el-card，它们等分一行，但是由于两个卡片的内容长度不确定，因此上述代码在运行的时候会因为两个卡片的内容长度不一致导致两个卡片的高度出现一高一低的现象。

栅格提供了flex模式布局，因此我们可以在el-row中添加```type=flex```即可，同时因为flex布局会以最右侧的盒子的高度作为基准，我们还需要将最右侧的卡片设置一个高度，具体代码如下：

```vue
<template>
    <div>
        <el-row type="flex">
            <el-col :span='12'>
                <el-card class="box-card">
                    <div slot="header" class="card-header">
                        <span>我是第一个卡片</span>
                    </div>
                    <div class=card-body>
                        <p>11111</p>
                        <p>11111</p>
                        <p>11111</p>
                        <p>11111</p>
                        <p>11111</p>
                    </div>
                </el-card>
            </el-col>
            <el-col :span='12'>
                <el-card class="box-card">
                    <div slot="header" class="card-header">
                        <span>我是第二个卡片</span>
                    </div>
                    <div class=card-body>
                        <p>222222222</p>
                        <p>222222222</p>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<scripts>

</scripts>

<style scoped>
.box-card {
    height: 100%;
}
</style>
```