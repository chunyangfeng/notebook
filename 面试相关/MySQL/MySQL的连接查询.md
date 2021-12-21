#### 内连接(inner join)

**关键字**：inner  join   on 

**语句**：```select * from a_table a inner join b_table b on a.a_id = b.b_id;```

**说明**：组合两个表中的记录，返回关联字段相符的记录，也就是返回两个表的交集部分。

#### 左连接(left join)

**关键字**：left join on / left outer join on

**语句**：```SELECT  * FROM a_table a left join b_table b ON a.a_id = b.b_id;```

**说明**： left join 是left outer join的简写，它的全称是左外连接，是外连接中的一种。 左(外)连接，左表(a_table)的记录将会全部表示出来，而右表(b_table)只会显示符合搜索条件的记录。右表记录不足的地方均为NULL。

#### 右连接(right join)

**关键字**：right join on / right outer join on

**语句**：```SELECT  * FROM a_table a right outer join b_table b on a.a_id = b.b_id;```

**说明**：right join是right outer join的简写，它的全称是右外连接，是外连接中的一种。与左(外)连接相反，右(外)连接，左表(a_table)只会显示符合搜索条件的记录，而右表(b_table)的记录将会全部表示出来。左表记录不足的地方均为NULL。

#### 全连接(full join)

**关键字**：union /union all

**语句**：
```SQL
(select colum1,colum2...columN from tableA ) union (select colum1,colum2...columN from tableB )
或 
(select colum1,colum2...columN from tableA ) union all (select colum1,colum2...columN from tableB )；
```

**说明**：
1. 通过union连接的SQL它们分别单独取出的列数必须相同；
2. 不要求合并的表列名称相同时，以第一个sql 表列名为准；
3. 使用union 时，完全相等的行，将会被合并，由于合并比较耗时，一般不直接使用 union 进行合并，而是通常采用union all 进行合并；
4. 被union 连接的sql 子句，单个子句中不用写order by ，因为不会有排序的效果。但可以对最终的结果集进行排序；