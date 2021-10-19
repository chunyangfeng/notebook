#### 场景

用户登陆成功后，会把后端返回的token和username存入session，由于页面骨架布局需要展示用户名，但是骨架的header是一个子组件，在登陆成功前就已经创建完毕了，因此会出现登陆成功了，但是子组件无法正常获取session中的值，必须要刷新一下页面才会正常获取值

#### 方案
父组件
```vue
<template>
  <div>
    <header v-if="isRefresh"></header>
    <main-body></main-body>
    <footers></footers>
  </div>
</template>

<script>
export default {
    name: "index",
    data() {
        return {
            isRefresh: true
        }
    },
    mounted () {
        const username = login(.......)
        sessionStorage.setItem('username', username)
        
        this.isRefresh = false
        this.$nextTick(() => {
            this.isRefresh = true
        })
    }
}
</script>
```

子组件
```vue
<template>
  <div>
    <p>{{username}}</p>
  </div>
</template>

<script>
export default {
    name: "index",
    data() {
        return {
            username: sessionStorage.getItem('username') || 'Anonymous'
        }
    },
}
</script>
```

#### 结语
通过使用v-if来强制刷新子组件，让子组件正常获取session的值