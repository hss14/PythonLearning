#proj4: gather news: various sources including NNTP to various destinations
<br/>

*NOTICE:*
:    codes of this project have never being executed or tested because I didn't find a free NNTP server that supports the `newnews` method

---
<br/>
<br/>


##如何抽象 

- 本项目本身很简单，主要是学习怎样抽象，怎样把黏在一起的代码剥离结构，大大增加灵活性
- 从问题描述出发：(ch7.3  P125; P363)
	- 名词 → 类
	- 动词 → 方法， 形容词 → 特性
- 用 `NewsAgent` 类剥离前、后端：Source、Destination
	- 此处体现了python的多态基于 规则protocol：
	- 只要求每个源实现返回`NewsItem`对象的`getItem()`(生成器)方法
- 只有`__init__`一个方法的`NewsItem`类，相当于结构体，用于在前端、agent、后端中传递信息流

<br/><br/>
##零散知识点

### html:

- 链接到页面内部的超链接：

```html
<a href="#n">...</a> → <a name="n">...</a>   <!-- n 为任意数字 -->
```

- <pre>预格式化的文本，保留文本格式如空格和换行，常用于表示源代码</pre>


### `print >> fd, "string"` 打印到fd

### `email`模块：`message_from_string`方法，方便地直接提取主题和文本内容

### `textwrap`模块：`wrap`方法 用于 文本输出格式对齐
