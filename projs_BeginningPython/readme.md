#出了bug的知识点

##proj3: XML to website

### 元组
- `()`可以构造空元组，但构造一个元素的元组必须加逗号：
  - √：`(attrs,)` `attrs,`
  - ×：`(attrs)`
    
### 参数收集
用`*tuple`可用元组收集一组参数：
- 形参最后一个参数用`*params`，则可将实参传递进来的多余参数全部收进元组`params`中
- 实参用`*args`，则可将元组`args`中的元素匹配给形参为多个元素的函数

<br/>
<br/>

---
<br/>

#第二次实现中的改进

##proj3: XML to website

###Mix-in类
- 提供有限功能，用于和其他更具体的类一起继承
- 通过混入类+`getattr`（与proj1方法相同），自动调用相应方法，而不需要一坨if语句
 
###减少黏连性，提高复用度
单独的方法：`writeHeader()`,&nbsp;&nbsp;`writeFooter()`,&nbsp;&nbsp;`startDefault()`,&nbsp;&nbsp;`endDefault()`

<br/>
<br/>
<br/>
