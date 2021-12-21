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