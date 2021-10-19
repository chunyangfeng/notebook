#### router.push触发任务
如果在一个组件的mounted中会默认调用一个初始化函数：this.initial()，正常情况下都能正常实现

但是如果这个组件是通过router.push或者router.replace进入的，那么就会发现，此时的组件由于已经创建完毕，mounted不会再次执行

因此我们需要让router.push/replace也能触发初始化函数

##### 方法一
```vue
  watch: {
    $route() {
      this.initial()
    }
  },
```

##### 方法二
```vue
  beforeRouteEnter: (to, from ,next) => {
    next(vm => {
      vm.initial()
    })
  },
```

方法二比方法一的效率高，同时也是官方推荐使用的，但是尚未经过验证，后续验证完毕会补充此处笔记

#### 监听属性变化

```Vue
  data() {
      return {
          addFormControl: {
              form: {
                  value: '',
              }
          }
      }
  },
  watch: {
    'addFormControl.form.value': {
      handler(currentValue, oldValue) {
        console.log(`value has being changed: ${oldValue} to ${currentValue}`)
      },
      deep: true
    }
  },
```