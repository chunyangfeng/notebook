#### 创建节点
```sql
create (nodeName: labelName {k1: v1, ..., kn: vn})

e.g
create (zhangsan: Person {name: "zhangsan", age: 20})
```

#### 创建节点间的关系
```sql
create (nodeName)-[:relationshipName {k1: v1, ... kn, vn}]->(nodeName)

e.g

```

#### 删除所有数据
```sql
match (n) detach delete n
```

#### DDL
```sql
create (dept1: DEPARTMENT {name:"汽车事业部",id:"dept-1",level:0}),
(dept2: DEPARTMENT {name:"基础架构",id:"dept-1-1",level:1}),
(dept3: DEPARTMENT {name:"用户平台",id:"dept-1-2",level:1}),
(dept4: DEPARTMENT {name:"商业化",id:"dept-1-3",level:1}),
(dept5: DEPARTMENT {name:"运维",id:"dept-1-1-1",level:2}),
(dept6: DEPARTMENT {name:"中间件",id:"dept-1-1-2",level:2}),
(dept7: DEPARTMENT {name:"合伙人管理",id:"dept-1-2-1",level:2}),
(dept8: DEPARTMENT {name:"金融管理",id:"dept-1-2-2",level:2}),
(user1: USER {name:"张三", age: 20, id: "user-1"}),
(user2: USER {name:"李四", age: 20, id: "user-2"}),
(user3: USER {name:"王五", age: 20, id: "user-3"}),
(user4: USER {name:"赵六", age: 20, id: "user-4"}),
(user5: USER {name:"Tom", age: 20, id: "user-5"}),
(ecs1: ECS {inst_id: "ecs-1", ip: "192.168.1.1"}),
(ecs2: ECS {inst_id: "ecs-2", ip: "192.168.1.2"}),
(ecs3: ECS {inst_id: "ecs-3", ip: "192.168.1.3"}),
(ecs4: ECS {inst_id: "ecs-4", ip: "192.168.1.4"}),
(ecs5: ECS {inst_id: "ecs-5", ip: "192.168.1.5"}),
(dept1)-[:INCLUDE]->(dept2),
(dept1)-[:INCLUDE]->(dept3),
(dept1)-[:INCLUDE]->(dept4),
(dept2)-[:INCLUDE]->(dept5),
(dept2)-[:INCLUDE]->(dept6),
(dept3)-[:INCLUDE]->(dept7),
(dept3)-[:INCLUDE]->(dept8),
(dept5)-[:INCLUDE]->(user1),
(dept5)-[:INCLUDE]->(user2),
(dept7)-[:INCLUDE]->(user3),
(dept8)-[:INCLUDE]->(user4),
(dept8)-[:INCLUDE]->(user5),
(user1)-[:MANAGE]->(ecs1),
(user1)-[:MANAGE]->(ecs2),
(user2)-[:MANAGE]->(ecs2),
(user3)-[:MANAGE]->(ecs3),
(user4)-[:MANAGE]->(ecs4),
(user5)-[:MANAGE]->(ecs5)
```

#### 查询节点
```sql
match (n: User) where n.name='Tom' return n

match (e:ECS) -[:MANAGE]-(u:USER) where e.ip="192.168.1.2"  return u
```
