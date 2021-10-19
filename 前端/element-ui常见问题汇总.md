#### 解决el-aside中的menu宽度多出1px的问题

```css
.el-menu {
    border-right-width: 0;
}
```

#### this.$confirm中的内容换行

```vue
    data(){
        return {
            checkbox: {
                selected: [],
            }
        }
    },
    
    allCheck() {
      this.$confirm('提示', {
        confirmButtonText: '是的',
        cancelButtonText: '不是',
        message: this.$createElement('div', {}, this.checkbox.selected.map(obj => {
          return this.$createElement('p', null, obj)
        })),
        type: 'warning',
      }).then(() => {
        this.$message.success('开始进行迁移检查...')
        this.checkbox.selected.forEach(item => {
          console.log(item)
        })
      })
    }
```

#### el-table中设置switch

如果需要在el-table中设置switch，并通过switch修改该行的值，则具体代码如下
```vue
<template>
  <div class="app-migrate">
    <el-table
        :data='migrateListData'
        border
        style="width: 100%">
      <el-table-column align="center" label="迁移状态">
        <template slot-scope="scope">
          <el-switch
              style="display: block"
              v-model="scope.row.status"
              active-color="#13ce66"
              inactive-color="#ff4949"
              active-text="已完成"
              active-value="done"
              inactive-value="incomplete"
              @change="statusChange($event, scope.row.id)"
              inactive-text="未完成">
          </el-switch>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "index",
  data() {
    return {
      migrateListData: [],
    }
  },
  methods: {
    statusChange(value, id) {
      console.log(value)
      console.log(id)
    },
  },
}
</script>

<style scoped>

</style>
```

通过```@change="statusChange($event, scope.row.id)"```监听switch状态的变化，其中```$event```是switch变化后的值