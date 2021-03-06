# python-gui-wxpython


* python GUI 似乎没有[electron+vue]好，列下大体框架有时间在研究。

## wxPython学习教程

[官方文档](http://wiki.wxpython.org/Getting%20Started)

[CSDN教程（推荐）](https://blog.csdn.net/chenghit/article/details/50421090)

[CSDN教程](https://blog.csdn.net/shaxiaozilove/article/details/51638054)


## 环境要求

python3.7
wxPython4.1.1

>安装python、pip

## 更新pip

```python
pip install --upgrade pip
```

## 安装依赖
```python
pip install requirements.txt
```

## 运行

```python
python test_main.py
```

## 参数

'''
    [参数介绍]
    parent = None   #父元素，假如为None，代表顶级窗口。
    id = None       #组件的标识，唯一，假如id为-1代表系统分配id。
    title=None      #frame窗口的标题栏。
    value = None    #文本框当中的内容。
    GetValue        #获取文本框的值。
    SetValue        #设置文本框的值。
    pos = None      #组件的位置，就是组件左上角点距离父组件或者桌面左和上的距离。
    size = None     #组件的尺寸，宽高。
    style = None    #组件的样式。
    name = None     #组件的名称，也是用来标识组件的，但是用于传值。
'''

## 窗口程序的基本框架

```python
    import wx
    app = wx.App(False) #创建1个APP，禁用stdout/stderr重定向
    frame = wx.Frame(None, wx.ID_ANY, "Hello, World!")  #这是一个顶层的window
    frame.Show(True)    #显示这个frame
    app.MainLoop()
```
![img](./static/demo.jpg)
|代码|	说明|
|--|--|
|app = wx.App(False)	|每一个 wxPython 应用程序都是一个 wx.App 实例。对于大多数的简单程序，直接实例化 wx.App 即可。但如果你希望创建一个复杂的应用程序，那么可以对 wx.App class 做一些扩展。”False” 参数意味着“不要把 stdout 和 stderr 信息重定向到窗口”，当然也可以不加 “False” 参数。|
|frame = wx.Frame(None, wx.ID_ANY, “Hello, World!”)	|完整的语法是 x.Frame(Parent, Id, Title)。在本例中，我们使用 “None” 来表示这个frame是顶层的框架，没有父框架；使用 “wx.ID_ANY” 让 wxWidgets 来给我们挑选一个ID。|
|frame.Show(True)	|显示这个Frame|
|app.MainLoop()	|运行这个应用程序|

>如果工作在windows平台的话，建议同时安装pywin32模块。pywin32允许你像VC一样的使用python开发win32应用，更重要的是，可以用它直接操控win32程序，捕捉当前窗口、获取焦点等


## 组件

### 菜单栏
添加一个菜单栏MenuBar

### 状态栏
### 静态文本控件
### 文本输入控件
### 多行文本控件 wx.TE_MULTILINE
### 创建字体
### 按钮
* 1.文本按钮 
```python
wx.Button(parent, id, label, pos, size=wxDefaultSize, style=0, validator, name="button")
```

* 2.位图按钮
```python
wx.BitmapButton(panel, -1, bmp, pos=(10, 20))
```

* 3.开关按钮（toggle button）
```python
wx.ToggleButton(panel, -1,u"开关", pos=(10, 150))
```
当你按下一个开关按钮（toggle button）时，它将一直保持被按下的状态直到你再次敲击它。

在wx.ToggleButton与父类wx.Button之间只有两个区别：
    a、当被敲击时，wx.ToggleButton发送一个EVT_TOGGLEBUTTON事件。
    b、wx.ToggleButton有GetValue()和SetValue()方法，它们处理按钮的二进制状态。

* 4.通用按钮
```python
```

### 滑块（slider）
```python
```

### 微调控制器（wx.SpinCtrl）
```python
```

### 进度条 wx.Gauge
```python
```

### 复选框 wx.CheckBox
```python
```

### 单选按钮（radio button）
```python
```

### 列表框wx.ListBox
```python
```

### 合并复选框和列表框 wx.CheckListBox
```python
```

### 框架 wx.Frame
```python
```

### MDI框架
```python
```

### 小型框架
```python
```

### 分割窗 wx.SplitterWindow
```python
```

### 模式对话框
```python
```
* 1.用对话框显示选项列表 wx.SingleChoiceDialog

* 2.在对话框上显示进度条

* 3.文件选择对话框 wx.FileDialog

* 4.使用文件对话框的函数：

* 5.选择一个目录

* 6.字体选择对话框

* 7.颜色对话框

* 8.使用户能够浏览图像


9.向导


10.启动提示


11.图像


12.如何改变光标


```python
```



## 注意事项

1.mac无法安装win32api
2.常用控件总结
3.

## 其他

* 1.不同GUI对比
'''
    python gui（图形化）常用模块介绍
    [Tkinter]
    python最简单的图形化模块，总共只有14种组建，（也叫Tk接口）是Tk图形用户界面工具包标准的Python接口。
    Tk是一个轻量级的跨平台图形用户界面（GUI）开发工具。
    Tk和Tkinter可以运行在大多数的Unix平台、Windows、和Macintosh系统。
    
    [Pyqt]
    python最复杂也是使用最广泛的图形化，PyQt是Qt库的Python版本。PyQt是用SIP写的。PyQt 提供 GPL版和商业版。
    
    [Pywin]
    python windows 下的模块，摄像头控制(opencv)，常用于外挂制作，Windows Pywin32允许你像VC一样的形式来使用PYTHON开发win32应用。
    代码风格可以类似win32 sdk，也可以类似MFC，由你选择。如果你仍不放弃vc一样的代码过程在python下，那么这就是一个不错的选择。
    
    [wxPython]
    最流行的Python GUI开发框架之一，基于[wxWidgets]，是一个C++编写的跨平台GUI库，除了标准的对话框，还提供一个2D路径绘制API，支持多种文件格式以及文本编辑和字处理widgets。
    wxPython是Python 语言的一套优秀的 GUI 图形库，允许 Python 程序员很方便的创建完整的、功能键全的 GUI 用户界面。
    作为优秀的[跨平台]GUI库wxWidgets的Python封装和Python模块的方式提供给用户的。
    就如同Python和wxWidgets一样，wxPython也是一款开源软件，并且具有非常优秀的跨平台能力，能够运行在32位windows、绝大多数的Unix或类Unix系统、Macintosh OS X上。

'''

* 2.冻结第三方库，就是将所有第三方库及版本号保存到requirements.txt文本文件中
```shell
pip freeze > requirements.txt
```



