```vue
  watch: {
    $route() {
      this.getAuth()
    }
  },
```

在push的组件里监听$route即可

```vue
  beforeRouteEnter: (to, from ,next) => {
    next(vm => {
      vm.getAuth()
    })
  },
```

上面这种方法理论上也行，而且比第一种效率更高，但是测试上没实现效果。暂时不研究了，后续抽空再说吧