#### 简介

大型项目中，总是会有很多的全局样式，在一整个完整项目中，统一风格，这时候就需要定义一个全局样式，并在使用时引入。

当项目特别大时，管理就会变的麻烦，我们就需要使用全局变量这种引入方式，进行全局样式的统一管理。

本文以less为例，介绍vue-cli3.0中如何启用全局样式变量。

#### 环境
```Shell
vue-cli: 3.0
less
```

#### 配置

1. 安装less
```shell
npm install less, less-loader
```

2. 安装插件
```shell
npm install vue-cli-plugin-style-resources-loader
npm install style-resources-loader
```

3. 配置
编辑vue.config.js(vue-cli3默认没有这个文件，创建它(和src目录平级))
```javascript
/*
全局vue-cli配置
 */

const path = require("path")

module.exports = {
    pluginOptions: {
        // 配置less全局变量
        "style-resources-loader": {
            preProcessor: 'less',
            patterns: [path.resolve(__dirname, "./src/assets/css/global.less")]
        }
    }
};
```

4. 使用
编辑src/assets/css/global.less，定义全局变量配置
```less
@test-color: blue;
```

在文件中直接使用
```less
.layout-header {
  background-color: @test-color;
}
```