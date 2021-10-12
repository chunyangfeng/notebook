#### 资料参考
```shell
https://neo4j.com/docs/cypher-manual/current/
```

#### 创建用户
```shell
# 切换至system库
use system

# 创建用户，参数1为用户名，参数2为密码，参数3为初次登录后是否需要修改密码
call dbms.security.createUser("gaia", "123456", false)

# 建议使用下面这种方式
create user gaia set password '123456'
```