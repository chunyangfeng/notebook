### 问题描述

通常情况下，如果Promise的then中出现了异常，那么这个异常会抛出来并被同级的catch捕获。现象就是既执行了一部分then中的代码，同时也会执行catch中的代码。

elementui中的confirm组件，在点击确认按钮时会进入正常的then代码中，而在点击取消按钮时则会进入catch代码中。

在此基础上，如果confirm的then中出现了未知异常，那么就会出现进入catch的现象，导致正常的confirm逻辑出现诡异的bug。

### 实例

```vue
<template>
<div>
  <el-button @click="btnClick">触发</el-button>
</div>
</template>

<script>
export default {
  name: "promiseTest",
  methods: {
    btnClick() {
      this.$confirm('消息确认', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'success'
      }).then(() => {
        // console.log(1/0)
        console.log('i am in promise then')
        throw new Error('手动抛出异常')
      }).catch((error) => {
        console.log('i am in promise catch')
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>

</style>
```

