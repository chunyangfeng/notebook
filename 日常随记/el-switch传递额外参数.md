```vue
                  <el-switch
                    @change="switchChange"
                    v-model="switch_value"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
```

默认情况下el-switch的@change会接受一个参数，这个参数是当前el-switch的值

有些情况下，可能需要对这个change事件传递其他的参数，比如表格的行数据，那么可以使用如下方式进行传递

```vue
                  <el-switch
                    @change="switchChange($event, props.row)"
                    v-model="switch_value"
                    active-color="#13ce66"
                    inactive-color="#ff4949">
                  </el-switch>
```

$event代表当前el-switch的值