#### 环境准备

```shell
centos: 7.9
neo4j: 4.3.5
```

#### 安装

##### 配置yum源

```shell
rpm --import https://debian.neo4j.com/neotechnology.gpg.key
cat <<EOF >  /etc/yum.repos.d/neo4j.repo
[neo4j]
name=Neo4j RPM Repository
baseurl=https://yum.neo4j.com/stable
enabled=1
gpgcheck=1
EOF
```

##### 安装JDK11

由于neo4j对jdk版本有要求，neo4j-4.3.5对应使用jdk11，因此需要提前准备

检查当前系统是否存在jdk

```shell
java -version
```

如果存在，则卸载
```shell
yum remove java-xx-openjdk -y
```

安装jdk11
```shell
yum install java-11-openjdk -y
```

安装完成后检查是否为jdk11
```shell
java -version

openjdk version "11.0.12" 2021-07-20 LTS
OpenJDK Runtime Environment 18.9 (build 11.0.12+7-LTS)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.12+7-LTS, mixed mode, sharing)
```
##### 安装neo4j
```shell
yum install neo4j -y   # 社区版
yum install neo4j-enterprise -y  # 企业版
```

##### 修改配置文件
vim /etc/neo4j/neo4j.conf

```shell
# 去掉注释，让服务绑定在ip地址上
71 dbms.default_listen_address=0.0.0.0
```

##### 服务管理

开机自启动
```shell
systemctl enalbe neo4j
```

启动服务
```shell
systemctl start neo4j
```