#### 判断元素是否在数组中
```javascripts
const arr = ["apple", "banana", "orange", "purple"]

# 方法一
arr.includes("apple")  => true or false

# 方法二
arr.indexOf("apple") => -1 or other number
```

#### 指定数组索引删除/增加元素
```javascripts
const array = ["a", "b", "c", "d", "e"]

# 删除索引为1的元素，第一个参数为索引的起始位置，第二参数为从索引起始
# 位置开始删除元素的个数

array.splice(1, 1)  => ["b"]

# 在索引为2的位置插入元素'test'，前两个参数和删除时代表的含义一致，区别是如果第
# 二个参数设置为0，则表示不删除元素，第三个参数及以后的参数为待插入的元素

array.splice(2, 0, 'test')  => []
```

**需要注意的是splice操作会修改原数组**

#### 获取Object的所有key/value
```javascripts
const dict = {"apple": 5, "orange": 3, "banana": 4, "cherry": 78}

# 获取所有key
Object.keys(dict)  => ['apple', 'orange', 'banana', 'cherry']

# 获取所有value
Object.values(dict) => [5, 3, 4, 78]
```

#### 根据Object的value寻找key
```javascripts
const getKey = (obj, value, compare = (first, second) => first === second) => {
    return Object.keys(obj).find(key=>compare(obj[key], value))
}

const dict = {"apple": 5, "orange": 3, "banana": 4, "cherry": 78}

getKey(dict, 78)  => 'cherry'
```

**需要注意的是，上述方案对于嵌套结构是无效的，如果Object的value是一个复杂的嵌套结构，那么在进行value的比较的时候会失败，因为{"key": 1} === {"key": 1}的真值为false**
