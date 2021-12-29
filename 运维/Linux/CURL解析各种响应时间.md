### 概述

有时候我们需要对某一个站点进行全方位的访问链路检测，可以通过curl命令，轻易获取到整个链路中的各种响应时间，方便我们进行问题的分析。

```shell
curl -o /dev/null -s -w "域名解析时间：%{time_namelookup}\n
下载速度：%{speed_download}\n
连接时间：%{time_connect}\n
开始传输时间：%{time_starttransfer}\n
花费总时长：%{time_total}\n
响应状态码：%{http_code}"  http://www.baidu.com
```

字段 | 说明
--- | ---
time_namelookup | DNS解析时间,从请求开始到DNS解析完毕所用时间
time_connect   |连接时间，从开始到建立TCP连接完成所用时间，包括前边DNS解析时间，如果需要单纯的得到连接时间，用这个 time_connect 时间减去前边 time_namelookup 时间。以下同理
time_starttransfer   |开始传输时间。在发出请求之后，Web 服务器返回数据的第一个字节所用的时间
time_total   |总时间，按秒计，精确到小数点后三位
http_code   |http状态码，如200成功,301转向,404未找到,500服务器错误等。
speed_download   |下载速度，单位 字节每秒 byte/s
