# -*- coding:utf-8 -*-
# Author: suke
# At 2015/11/10 16:09

# 闭包将会捕捉内层函数执行所需的整个环境
# enclose.py
import foo

def wrapper():
    filename = 'enclose.py'
    def show_filename():
        return 'filename: %s' % filename
    print foo.call_func(show_filename)  # 输出 filename: enclose.py
wrapper()
# 1、Local - 本地函数(show_filename)内部，通过任何方式赋值的，而且没有被
#   global关键字声明为全局变量的filename变量；
# 2、Enclosing - 直接外围空间(上层函数wrapper)的本地作用域，查找filename变量
#   (如果有多层嵌套，则由内而外逐层查找，直至最外层的函数)；
# 3、Global - 全局空间(模块enclosed.py)，在模块顶层赋值的filename变量；
# 4、Builtin - 内置模块(__builtin__)中预定义的变量名中查找filename变量；
