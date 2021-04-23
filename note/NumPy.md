#### ndarray
- 创建一个ndarray: `np.array(p_object, dtype=None, *args, **kwargs)`
- 构造ndarray数据类型对象: `numpy.dtype(object, align, copy)`
- np数组属性:
  - 维度: `ndarray.ndim`
  - 形状(如m行n列): `ndarray.shape`
  - 元素类型: `ndarray.dtype`
  - 元素大小(以字节为单位): `ndarray.itemsize`
  - ndarray对象的内存信息: `ndarray.flags`
  - ndarray元素的实部: `ndarray.real`
  - ndarray 元素的虚部: `ndarray.imag`
- np创建数组:
  - 创建元素为空(默认内存值)的ndarray: `np.empty(shape, dtype='float', order='C')`
  - 创建元素值为0的ndarray: `np.zeros(shape, dtype='float', order='C')`
  - 创建元素值为1的ndarray: `np.ones(shape, dtype='float', order='C')`
- np从已有数组创建数组
  - `numpy.asarray(a, dtype = None, order = None)`
  - `numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)`
  - `numpy.fromiter(iterable, dtype, count=-1)`
- np从数值范围创建数组
  - numpy.arange(start, stop, step, dtype)
  - 生成等差数列: np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
  - 生成等比数列: np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
- np切片和索引:
  - ```python
    s = slice(start, end, step)  #来自标准库
    e = ndarray[s]
    ```
  - ```
    e = ndarray[start:end:step]
    ```
  - start,end与step均可省略
  - ndarray[index]可直接取得对应索引的元素
  - `...` 如果在行位置使用省略号，它将返回包含行中元素的 ndarray. 如a[...,1] 或 a[1,...]
- np高级索引--除了之前看到的用整数和切片的索引外，数组可以由整数数组索引、布尔索引及花式索引
  - 整数数组索引
    ```python
     import numpy as np
     # 获取数组中(0,0)，(1,1)和(2,0)位置处的元素
     a = np.array([[1,  2],  [3,  4],  [5,  6]]) 
     b = a[[0,1,2],  [0,1,0]]
     print (b)  #[1  4  5]
    
     x = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8],[9, 10, 11]])
     rows = np.array([[0,0],[3,3]]) 
     cols = np.array([[0,2],[0,2]]) 
     y = x[rows,cols]  
     print (y)    #[[ 0  2] [ 9 11]]
    
    # 在索引中还可以加入...或 : ,来表示索引范围
    ```
  - 布尔索引--布尔索引通过布尔运算（如:比较运算符）来获取符合指定条件的元素的数组
  ```python
  import numpy as np
  
  a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
  y = a[a > 5]    # [ 6  7  8  9 10 11]
  ```
  - 花式索引--花式索引根据索引数组的值作为目标数组的某个轴的下标来取值
    - 传入顺序索引数组
      ```python
       import numpy as np  
       x = np.arange(32).reshape((8, 4))
       print(x)
       print('\n')
       print(x[[4, 2, 1, 7]])
      ```
    - 传入倒序索引数组`x[[-4, -2, -1, -7]`
    - 传入多个索引数组(要使用np.ix_)
- 广播(Broadcast)--广播(Broadcast)是numpy对不同形状(shape)的数组进行数值计算的方式,对数组的算术运算通常在相应的元素上进行
    ```python
    import numpy as np
    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])
    c = a * b    # c = [10  40  90 160]
    ```
  运算中的2个数组的形状不同时, numpy 将自动触发广播机制.广播规则:
  - 让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
  - 输出数组的形状是输入数组形状的各个维度上的最大值。
  - 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
  - 当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。
- 迭代数组--当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。
- 数组操作
  - 修改数组形状
    - np.reshape(arr, newshape, order='C')
    - ndarray.flat  一个元素迭代器
    - ndarray.flatten(order='C')  返回一份数组拷贝, 对拷贝做更改不会影响原数组
    - np.ravel(a, order='C')  展平一个数组
  - 翻转数组
    - numpy.transpose(arr, axes)
    - numpy.rollaxis(arr, axis, start)  向后滚动特定的轴到一个特定位置
    - numpy.swapaxes(arr, axis1, axis2)  用于交换数组的两个轴
  - 修改数组维度
    - np.broadcast()
    - np.broadcast_to()
    - np.expand_dims()
    - np.squeeze()
    - np.concatenate()
    - np.stack()
    - np.hstack()
    - np.vstack()
  - 分割数组
    - np.split()
    - np.hsplit()
    - np.vsplit()
  - 数组元素的添加与删除
    - np.resize()
    - np.append()
    - np.insert()
    - np.delete()
    - np.unique()
