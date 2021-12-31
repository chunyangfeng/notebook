#### 概述

docker服务默认使用root用户，docker组运行，如果我们的机器不允许使用root权限运行，或者不允许创建docker用户，
那么我们就需要修改这个配置，让docker服务启动的时候使用指定的用户和组运行。

#### 配置

```shell
docker version: 19.03
os: CentOS 7.3
```

#### 操作

修改文件 ```vim /usr/lib/systemd/system/docker.socket```

```shell
[Unit]
Description=Docker Socket for the API
PartOf=docker.service

[Socket]
ListenStream=/var/run/docker.sock
SocketMode=0660
SocketUser=work
SocketGroup=work

[Install]
WantedBy=sockets.target
```

将文件中的```SocketUser```和```SocketGroup```修改为指定的用户和组,重启docker服务即可

```shell
systemctl restart docker
```
