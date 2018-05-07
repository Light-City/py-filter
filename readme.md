# 变量的过滤器(filter)的使用

```python
语法格式：      {{obj|filter:param}}
1.add:给变量加上相应的值
2.addslashes:给变量中的引号前加上斜线
3.capfirst:首字母大写
4.cut：从字符串中移除指定的字符
5.date:格式化日期字符串
6.default:如果值是False,就替换成设置的默认值，否则就是用本来的值
7.default_if_none:如果值是None，就替换成设置的默认值，否则就使用本来的值
```
>urls.py

```python
from django.contrib import admin
from django.conf.urls import url
from tem import views
urlpatterns = [
    url(r'admin/$', admin.site.urls),
    url(r'query/',views.query),
]
```
>views.py

```python
from django.shortcuts import render
import datetime
# Create your views here.
class Animal(object,):
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex

def query(request):
    l=["存","正","参"]
    d={'name':'见','age':12,'sex':'M'}
    c=Animal('alex','M')
    test='world'
    test1='hello kitty'
    t=datetime.datetime.now()
    e=[]
    a='<a href=''>click</a>'
    return render(request,'index.html',locals())
```

>index.html

```html
<h1>hello {{ l.1 }}</h1>
<h1>hello {{ l.2 }}</h1>
<h1>hello {{ d.name }}</h1>
<h1>hello {{ d.age }}</h1>
<h1>hello {{ d.sex }}</h1>
<h1>hello {{ c.name }}</h1>
<h1>hello {{ c.sex }}</h1>
<h1>{{ d.name }}的真实年龄:{{ d.age|add:12 }}</h1>
<h1>hello {{ test|capfirst }}</h1>
<h1>{{ test1 }}</h1> <!-- helo kitty-->
<h1>{{ test1|cut:' ' }}</h1> <!-- 去除空格 helokitty-->
<h1>{{ t }}</h1>
<h1>{{ t|date:'Y-m-d' }}</h1>
<h1>{{ e }}</h1>
<h1>{{ e|default:'空列表' }}</h1> <!-- 若e为空列表，则过滤default用后面值来代替 -->
<h1>{{ e|default_if_none:'空列表' }}</h1> <!-- 若e不为空列表，则过滤default用后面值来代替 -->
<h1>{{ a }}</h1>
<h1>{{ a|safe }}</h1>
<!-- 与上面<h1>{{ a|safe }}</h1>等价 -->
{% autoescape off %}
<h1>{{ a }}</h1>
{% endautoescape %}
```