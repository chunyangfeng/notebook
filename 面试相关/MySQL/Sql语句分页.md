#### 语法

```SQL
select * from table limit (curPage-1)*pageSize,pageSize;
```

其中```currPage```表示当前页数，```pageSize```表示每页的数量

如：
```SQL
select * from student limit (5 - 1) * 10, 10;
```

上述例子表示从student表中查出第5页的所有数据，其中每页数量为10条。