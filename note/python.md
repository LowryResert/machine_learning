### python基础

#### 关键字
- pass 什么事都不做，相当于占位符，防止代码编译出错
- None 相当于null
- def

#### **乘方
- 2**10 = 1024

#### /与//
- /计算结果为整数， //(地板除)计算结果只取整数部分

#### ""与'',''''''
- 没有区别，括中内容都是字符串
- '''xxx'''可以表示多行内容

#### 标准库
- **help(funcName) 获取函数说明**
- len() 长度
- int(val) 类型转换
- type(val) 类型——不会认为子类是一种父类类型，不考虑继承关系。
- isinstance(val, type)—返回值True/False,考虑继承关系。
- list(val) 转为list
- range(val) 生成0 - val-1的序列

#### 数据类型
- 整数
- 浮点数
- 字符串
- 布尔值 (包括True和False两个值，支持 and, or, not 三种运算)
- 空值 None
- 变量 (动态语言—变量类型不固定√，静态语言—变量类型固定)
- list——列表，其中元素类型可以不同
    - 初始化空列表 listName = []
    - len(listName) 列表长度
    - listName[i],listName[-i]
    - listName.append(elem) 追加到列表末尾
    - listName.insert(idx, elem) 插入到index位置
    - listName.pop(i) 删除指定元素，参数为空删除末尾元素
- tuple——元组，一旦初始化，不可更改，允许元素类型不同
    - 初始化:tupleName = ('abc', 'bcd', 'cdf').定义一个元素的元组:t = (1,)加一个逗号来消除歧义，避免被解释为t=1
    - tupleName[i],tupleName[-i]仅支持按下标访问，不能修改任何值
    - tuple“可变”的情况:
        ```
        t = ('a', 'b', ['A', 'B'])
        t[2][0] = 'X' 
        t[2][1] = 'Y'
        # 此时t = ('a', 'b', ['X', 'Y'])
        ```
    - 故tuple不可变指的是tuple中每个元素的指向不可变
- dict——字典(即map) key-value
    - 判断字典中是否存在这个key-value, 返回bool值: key in dictName
    - 取值1: dictName[key], 若key不存在会报错
    - 取值2: dictName.get(key), 若不存在，返回None
    - dictName.pop(key) 删除元素
- set——集合，不重复
    - setName.add(val) 添加
    - setName.remove(val) 删除
  
#### 函数
- python允许多个返回值，但是这是一个假象，其实返回的是一个元组。返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
- 默认参数 def funcName(arg1, arg2=x)
    - 必选参数在前，默认参数在后，否则Python的解释器会报错.
    - 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
    - 定义默认参数要牢记一点：**默认参数必须指向不变对象**(具体的坑，见 https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888)
- 可变参数 def funcName(*vals)
    - 在参数前加*号，被调函数实际接收到的是tuple，上例甚至可以没有参数
    - 如果已有list或tuple要调用可变参数，写法可如：funcName(*listOrTupleName)
- 关键字参数——关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
    - 详细见https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888
    - 关键字参数获得实际参数(任意多个key-value组成的dict)的一份拷贝，改变形参，不会改变实参的值
- 命名关键字参数 可以限制关键字参数的名字,详细见以上link  
- 参数组合
    - 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用
    - 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
    - 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差。
- 可变参数与关键字参数
    - *args是可变参数,接收的是一个tuple
    - **kw是关键字参数,接收的是一个dict

#### 高级特性
- 切片
    - 对于list或tuple,取指定索引范围元素: listTupleName[startIdx:endIdx:interval]
    - startIdx为0,或者endIdx为最后一个元素可以省略,形如:listTupleName[:endIdx], listTupleName[startIdx:], listTupleName[:]
    - 支持负数索引
    - 与Java中substring方法一样, 区间前闭后开
    - interval指间隔,即每interval个元素取一个,可以省略
    - 切片不仅支持list和tuple,也支持str.(str可以看成一种list)
  
#### 迭代
- for val in obj
- 在python中,只要是可迭代对象，无论有无下标，都可以迭代
- 可迭代对象有: list, tuple, str, dict, set, generator
#### 列表生成式
```python
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = list(range(1, 11))

#eg.计算[1x1, 2x2, 3x3, ..., 10x10]
#方法一,循环
l = []
for x in range(11):
    l.append(x * x)
#方法二,列表生成式
l = [x * x for x in range(11)]

#不仅如此,还可以在生成式中加 if判断,两层循环等
l = [x * x for x in range(1, 11) if x % 2 == 0]
#l=[4, 16, 36, 64, 100]
l = [m + n for m in 'ABC' for n in 'XYZ']
#l=['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

#### 生成器 generator
- 方法一:创建一个generator，只要把一个列表生成式的[]改成()，就创建了一个generator
```python
g = (x * x for x in range(10))
#g=<generator object <genexpr> at 0x1022ef630>

#获取生成器中下一个值
next(g)

#遍历生成器
for x in g:
    print(x)
```
- 方法二:yield关键字,详细见 https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128

#### 迭代器 iterator
- isinstance(val, Iterable) 判断val是否可迭代
- 凡是可作用于for循环的对象都是Iterable类型
- 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
- 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
- Python的for循环本质上就是通过不断调用next()函数实现的











