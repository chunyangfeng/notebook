##### 更新新的配置到supervisord

```Shell
supervisorctl update
```

##### 重新启动配置中的所有程序

```Shell
supervisorctl reload
```

##### 启动某个进程(program_name=你配置中写的程序名称)

```Shell
supervisorctl start program_name
```

##### 查看正在守候的进程

```Shell
supervisorctl
```

##### 停止某一进程 (program_name=你配置中写的程序名称)

```Shell
pervisorctl stop program_name
```

##### 重启某一进程 (program_name=你配置中写的程序名称)

```Shell
supervisorctl restart program_name
```

##### 停止全部进程

```Shell
supervisorctl stop all
```