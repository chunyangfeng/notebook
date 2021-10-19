##### form 	
一个从POST和PUT请求解析的 MultiDict（一键多值字典）。

##### args	

MultiDict，要操作 URL （如 ?key=value ）中提交的参数可以使用 args 属性:

searchword = request.args.get('key', '')
##### values 	
CombinedMultiDict，内容是form和args。 
可以使用values替代form和args。

##### cookies	
请求的cookies，类型是dict。

##### stream	
在可知的mimetype下，如果进来的表单数据无法解码，会没有任何改动的保存到这个 stream 以供使用。很多时候，当请求的数据转换为string时，使用data是最好的方式。这个stream只返回数据一次。

##### headers 	
请求头，字典类型。

##### data 	
包含了请求的数据，并转换为字符串，除非是一个Flask无法处理的mimetype。

##### files 	
MultiDict，带有通过POST或PUT请求上传的文件。

##### environ 	
WSGI隐含的环境配置。

##### method	
请求方法，比如POST、GET。

##### path	
获取请求文件路径：/myapplication/page.html

##### script_root	 

##### base_url	
获取域名与请求文件路径：http://www.baidu.com/myapplication/page.html

##### url	
获取全部url：http://www.baidu.com/myapplication/page.html?id=1&edit=edit

##### url_root	
获取域名：http://www.baidu.com/

##### is_xhr	
如果请求是一个来自JavaScript XMLHttpRequest的触发，则返回True，这个只工作在支持X-Requested-With头的库并且设置了XMLHttpRequest。

##### blueprint 	
蓝图名字。

##### endpoint 	
endpoint匹配请求，这个与view_args相结合，可是用于重构相同或修改URL。当匹配的时候发生异常，会返回None。

##### json	
如果mimetype是application/json，这个参数将会解析JSON数据，如果不是则返回None。 
可以使用这个替代get_json()方法。

##### max_content_length	
只读，返回MAX_CONTENT_LENGTH的配置键。

##### module 	
如果请求是发送到一个实际的模块，则该参数返回当前模块的名称。这是弃用的功能，使用blueprints替代。

##### routing_exception = None
如果匹配URL失败，这个异常将会/已经抛出作为请求处理的一部分。这通常用于NotFound异常或类似的情况。

##### url_rule = None
内部规则匹配请求的URL。这可用于在URL之前/之后检查方法是否允许(request.url_rule.methods) 等等。 
默认情况下，在处理请求函数中写下 
print('request.url_rule.methods', request.url_rule.methods) 
会打印：
request.url_rule.methods {‘GET’, ‘OPTIONS’, ‘HEAD’}

##### view_args = None
一个匹配请求的view参数的字典，当匹配的时候发生异常，会返回None。

##### 其他方法	

get_json(force=False, silent=False, cache=True)

on_json_loading_failed(e)