# Installing TensorFlow_1.1 with CPU for Windows7
## 准备
* Windows7必须是64位版本
* Python 3.5.x
* MSVCP140.DLL. 如果没有, 需要安装 [Visual C++ 2015 redistributable (x64 version)](https://www.microsoft.com/en-us/download/details.aspx?id=53587)

## 安装步骤
### 打开cmd, 输入以下命令  
    C:\Users\sweetyu>pip3 install --upgrade tensorflow   
这一步我安装的时候出现了DLL相关的错误, 安装MSVCP140.DLL后故障排除.
  
## 验证安装
### 打开cmd, 输入以下命令  
    C:\Users\sweetyu>python
    >>>import tensorflow as tf
    >>>tf.__veision__
    '1.1.0'  
如果不报错则安装成功！

## 参考
* [Installing TensorFlow on Windows](https://www.tensorflow.org/install/install_windows)  
* [【简记】Windows安装TensorFlow 1.0版本](http://www.jianshu.com/p/7d719d781586)
