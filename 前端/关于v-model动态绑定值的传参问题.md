需求要写一组动态表单，用于对一个表单字段添加多个值，第一版代码如下：

```vue
<el-form>
    <el-form-item
        v-for="(host, index) in form.route_hosts"
        :label=`路由Hosts${index+1}`
        :key="host.id"
        :rules="{
                    required: true, message: '路由Host不能为空', trigger: 'blur'
                  }"
        :prop=`route_hosts[${index}].value`>
    <el-input v-model="host.value" placeholder="请输入访问路由的host"></el-input>
    </el-form-item>
</el-form>

data() {
  return {
    form: {
      route_hosts: [
        {value: ''}
      ]
    }
  }
}
```

信心满满的开始调试，结果就报错了，报错信息如下：

```shell
vue.esm.js?efeb:578 [Vue warn]: Property or method "host" is not defined on the instance but referenced during render. Make sure that this property is reactive, either in the data option, or for class-based components, by initializing the property. See: https://vuejs.org/v2/guide/reactivity.html#Declaring-Reactive-Properties.

found in

---> <DnsMgt> at src\views\project\src\source\dnsMgt.vue
       <RcContent> at src\layouts\content\src\content.vue
         <RcBody> at src\layouts\body\src\body.vue
           <App> at src\views\app.vue
             <Root>
```

说我定义的host不存在，但是翻来覆去，怎么看我的v-for都是正确的，调试了半天，最后脑子灵光一闪，开始怀疑两组反引号，改成如下代码：

```vue
<el-form>
    <el-form-item
        v-for="(host, index) in form.route_hosts"
        :label="`路由Hosts${index+1}`"
        :key="host.id"
        :rules="{
                    required: true, message: '路由Host不能为空', trigger: 'blur'
                  }"
        :prop="`route_hosts[${index}].value`">
    <el-input v-model="host.value" placeholder="请输入访问路由的host"></el-input>
    </el-form-item>
</el-form>

data() {
  return {
    form: {
      route_hosts: [
        {value: ''}
      ]
    }
  }
}
```

结果就好了。。。

