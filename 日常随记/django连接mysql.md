#### 环境

```shell
django == 3.2
mysql == 5.7
```

#### 操作

修改settings.py

```python
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dbtest',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOSTNAME': '192.168.56.103',
        'PORT': '3306'
    }
}
```

安装pymysql

```shell
pip install pymysql
```

设置pymysql连接

编辑settings.py同级的包文件```__init__.py```

```python
import pymysql

pymysql.install_as_MySQLdb()
```

完事儿
