```Python
class SlotsTest:
    __slots__ = ("name", "age")

    def __init__(self):
        self.name = "phoenix"
```

**测试name属性修改**
```Python
if __name__ == '__main__':
    slots = SlotsTest()
    print(f'修改前的name:{slots.name}')
    slots.name = "I am Tom!"
    print(f'修改后的name:{slots.name}')


# 输出
修改前的name:phoenix
修改后的name:I am Tom!
```

**测试age属性修改**
```Python
if __name__ == '__main__':
    slots = SlotsTest()
    slots.age = 24
    print(f'修改后的age:{slots.age}')
    
# 输出
修改后的age:24
```

**测试sex属性修改**
```Python
if __name__ == '__main__':
    slots = SlotsTest()
    slots.sex = "male"
    print(f'修改后的name:{slots.sex}')
    
# 输出
Traceback (most recent call last):
  File "F:/python-project/dj_test/leetcode/20210812.py", line 34, in <module>
    slots.sex = "male"
AttributeError: 'SlotsTest' object has no attribute 'sex'
```

由上述例子可见，```__slots__```中定义的方法或者属性，才将被类实例访问与修改。

如果直接用类对象访问，则```__slots__```不会生效，同时对继承的子类也不会生效。