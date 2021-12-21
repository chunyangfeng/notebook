*参考：https://yiyibooks.cn/xx/Django_1.11.6/ref/models/querysets.html*

本质上，可以创建、过滤、切片和传递QuerySet而不用真实操作数据库。 在你对查询集做求值之前，不会发生任何实际的数据库操作。

你可以使用下列方法对QuerySet求值：

- **Iteration**： QuerySet是可迭代的，它在首次迭代查询集时执行实际的数据库查询。
- **Slicing**： 正如在Limiting QuerySets中解释的那样， 可以使用Python 的序列切片语法对一个QuerySet进行分片。一个未求值的QuerySet进行切片通常返回另一个未求值的QuerySet，但是如果你使用切片的”step“参数，Django 将执行数据库查询并返回一个列表。对一个已经求值的QuerySet进行切片将返回一个列表。还要注意，虽然对未求值的QuerySet进行切片返回另一个未求值的QuerySet，但是却不可以进一步修改它了（例如，添加更多的Filter，或者修改排序的方式），因为这将不太好翻译成SQL而且含义也不清晰。
- Pickling/Caching. 序列化查询集的细节参见下面一节。本节提到它的目的是强调序列化将读取数据库。
- **repr()**： 当对QuerySet调用repr() 时，将对它求值。 这是为了在Python 交互式解释器中使用的方便，这样你可以在交互式使用这个API 时立即看到结果。
- **len()**： 当你对QuerySet调用len()时，将对它求值。正如你期望的那样，返回一个查询结果集的长度。
- **list()**： 对QuerySet调用list() 将强制对它求值。
- **bool()**： 测试一个QuerySet的布尔值，例如使用bool()、or、and 或者if 语句将导致查询集的执行。 如果至少有一个记录，则QuerySet为True，否则为False。

