```javascript
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