#proj3: XML to website
<br/>
<br/>


##万能的XML
- XHTML
- 表示音乐:&nbsp;&nbsp;&nbsp; <http://musicxml.org>
- 基于XML的PDF文档： ReportLab的Platypus工具
<br/>
<br/>

##处理XML的2类常用方法

- `SAX Parser`
  + 一次只存储文档的一小部分，简单快速，占用内存少；基于事件/event handler
  + 标准库模块为 `xml.sax`

- `DOM`
  + 构造文档树，较慢且耗内存；但如果希望操作整个文档结构的话很有用
  + 标准库模块为：
    - 标准DOM： `xml.dom` 
    - 简化DOM： `xml.dom.minidom`
    - SAX与DOM结合体，内存需求减少： `xml.dom.pulldom`    

- 中间状态
  + `pyRXP`: 简单快速，不使用DOM，但会建立完整文档树
  + `ElementTree`: 强大。标准库为`xml.etree`
<br/>
<br/>
  
  
##"hello world" of `sax`
  
```python
from xml.sax import ContentHandler
from xml.sax import parse
 
class WebsiteHandler(ContentHandler):      #有很多事件类型，这里只用到3个
    def startElement(self, name, attrs):   # attrs: 类字典类型 eg. `for key in attrs.keys():` `for k,d in attrs.items():`
      
    def endElement(self, name):
      
    def characters(self, chars):
    
parse( 'filename.xml', WebsiteHandler() )
```
<br/>
<br/>

##manipulate directory
```python
def ensureDirectory(self):
    path = os.path.join(*self.directory)
    if not os.path.isdir(path):
        os.makedirs(path)
```
<br/>
<br/>

##第二次实现中的改进
###Mix-in类
- 提供有限功能，用于和其他更具体的类一起继承
- 通过混入类+`getattr`（与proj1方法相同），自动调用相应方法，而不需要一坨if语句
 
###减少黏连性，提高复用度
单独的方法：`writeHeader()`,&nbsp;&nbsp;`writeFooter()`,&nbsp;&nbsp;`startDefault()`,&nbsp;&nbsp;`endDefault()`
<br/>
<br/>
<br/>

##在本project中用到而强化(出错)的知识点
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
