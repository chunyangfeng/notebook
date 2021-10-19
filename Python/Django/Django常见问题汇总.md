#### 合并QuerySet

有时候我们需要对两个QuerySet进行合并操作，操作方法如下
```python
from django.db.models import QuerySet
from app.models import MyModel

q1 = MyModel.objects.filter(id=1)
q2 = MyModel.objects.filter(id=2)

q = q1.union(q2)
```