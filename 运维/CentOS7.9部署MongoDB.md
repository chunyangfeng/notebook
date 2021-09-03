#### 系统环境

```Shell
操作系统：CentOS7.9
MongoDB版本：5.0
部署日期：2021-08-26
```

#### 参考资料

```Shell
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/
```

#### 部署流程

##### 创建repo文件

```Shell
[root@localhost soft]# touch /etc/yum.repos.d/mongodb-org-5.0.repo
```

```vim /etc/yum.repos.d/mongodb-org-5.0.repo```

repo文件内容如下：
```Txt
[mongodb-org-5.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/5.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-5.0.asc
```

##### 使用yum安装mongodb

```Shell
[root@localhost soft]# yum clean all
[root@localhost soft]# yum install mongodb-org -y
```

##### 启动mongodb

```Shell
[root@localhost soft]# systemctl start mongod
[root@localhost soft]# systemctl enable mongod
```

##### 测试安装结果

```Shell

[root@localhost soft]# mongosh
Current Mongosh Log ID: 612701d8c177d6b1aab65f1a
Connecting to:          mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000
Using MongoDB:          5.0.2
Using Mongosh:          1.0.5

For mongosh info see: https://docs.mongodb.com/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting:
   2021-08-25T22:51:37.626-04:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2021-08-25T22:51:37.626-04:00: /sys/kernel/mm/transparent_hugepage/enabled is 'always'. We suggest setting it to 'never'
   2021-08-25T22:51:37.626-04:00: /sys/kernel/mm/transparent_hugepage/defrag is 'always'. We suggest setting it to 'never'
------

test>
```

