# what I learned from bugs

### 元组 (proj3: XML to website)
- `()`可以构造空元组，但构造一个元素的元组必须加逗号：
  - √：`(attrs,)` `attrs,`
  - ×：`(attrs)`
    
### 参数收集 (proj3: XML to website)
用`*tuple`可用元组收集一组参数：
- 形参最后一个参数用`*params`，则可将实参传递进来的多余参数全部收进元组`params`中
- 实参用`*args`，则可将元组`args`中的元素匹配给形参为多个元素的函数

<br/><br/>

---
<br/>

# 模块化HOWTO

抽象 —— 把黏在一起的代码剥离为结构，减少黏连性，提高复用度，大大增加灵活性，使修改功能变得简单

### Mix-in类 (proj3: XML to website)
- 意在提供有限功能的类，用于和其他更具体的类一起继承
- 通过混入类+`getattr`（与proj1方法相同），自动调用相应方法，而不需要一坨if语句

### 用函数/方法剥离非常specific的功能 
- 如 打印html收尾的具体代码 装进方法：(proj3: XML to website)
    `writeHeader()`,&nbsp;&nbsp;`writeFooter()`,&nbsp;&nbsp;`startDefault()`,&nbsp;&nbsp;`endDefault()`

### 如何抽象 （proj4: gather news ）
- 从问题描述出发：(ch7.3  P125; P363)
	- 名词 → 类
	- 动词 → 方法， 形容词 → 特性
- 用 `NewsAgent` 类剥离前、后端：Source、Destination
	- 此处体现了python的多态基于 **规则protocol**：
	- 只要求每个源实现 返回`NewsItem`对象 的 `getItem()` (生成器)方法
- 只有`__init__`一个方法的`NewsItem`类，相当于结构体，用于在前端 → agent → 后端中传递信息流

<br/><br/>

---
<br/>


# 第二次实现中的改进





