#### 概述

在编写md文档时，有时候需要插入图片。

插图的基本格式为：

```shell
![ALT text](图片链接 "Title")

其中ALT text是图片加载失败时的描述文字，图片链接既可以是本地地址，
也可以是网络地址，还可以是图片的base64编码，可选的Title则是鼠标悬停时的提示文字。
```

基于此，MD插入图片有三种方式可以选择。

##### 插入本地图片

```shell
![picture](/home/phoenix/picture.jpg)
```

本地图片的源在物理机上，因此可移植性很差，MD文档一旦移植到另一台机器上，则有非常大的可能会因为图片路径不存在，导致图片加载失败。

##### 插入网络图片

```shell
![picture](https://github.com/phoneix/md/picture.jpg)
```

插入网络图片，则需要加载md文档的机器具备访问网络的能力，是一种比较常用的方式，单由于依赖网络，有时候也会出现图片加载失败的情况


#### 插入图片base64编码

```shell
![avatar][picture_id]


[picture_id]:data:image/png;base64,/9j/4AAQSkxsP1...
```

通过程序将图片转换为base64编码，则可以直接将图片存放在MD文档中，不需要依赖网络，也不需要依赖硬盘。

缺点就是图片的base64编码很长，非常的长，会使md文档变的臃肿，如果一篇MD文档中的图片数量非常多，则仍然建议使用插入网络图片的方式。

#### python3转换图片为base64编码的方法

```python
import base64

with open("/home/phoenix/picture.jpg", "rb") as f:
    base_code = base64.b64encode(f.read())
    print(base_code.decode())
```

需要注意的是，python3的base64模块生成的编码是纯粹的图片编码，而MD引用的编码，还需要在前面加上Data URI scheme：

```shell
data:image/png;base64,
```



