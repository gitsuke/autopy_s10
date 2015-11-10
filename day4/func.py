# -*- coding:utf-8 -*-
# Author: suke
# At 2015/11/10 16:01

import foo  # 导入foo.py

# func.py
filename = 'func.py'
def showt_filename():
    return 'filename: %s' % filename

if __name__ == '__main__':
    # 实际调用的位置是在foo.call_func函数中
    # 结果 filename: func.py
    # 很显然show_filename()函数使用的filename变量的值，
    # 是在与它相同环境(func.py模块)中定义的那个。
    # 尽管foo.py模块中也定义了同名的filename变量，
    # 而且实际调用show_filename的位置也是在foo.py的call_func内部。
    print foo.call_func(showt_filename)
