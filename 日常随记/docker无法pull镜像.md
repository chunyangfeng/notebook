#### 概述

按照官网方式安装docker之后，执行docker pull报以下错误：

```shell
ERROR: Get "https://registry-1.docker.io/v2/": EOF
```

需要修改默认的镜像源

创建文件```/etc/docker/daemon.json```

在文件中写入如下内容

```shell
{
    "registry-mirrors": ["https://registry.docker-cn.com", "https://pee6w651.mirror.aliyuncs.com"],
    "live-restore": true
}
```

重启docker

```shell
systemctl restart docker
```

