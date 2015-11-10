# -*- coding:utf-8 -*-
# Author: suke
# At 2015/11/10 11:35

import logging
logging.basicConfig(level=logging.INFO)

def add(a,b):
    return a+b

def checkParams(fn):
    def wrapper(a,b):
        # 检查a、b参数是否都是整数或者浮点数
        if isinstance(a,(int,float)) and isinstance(b,(int,float)):
            return fn(a,b)  # 调用fn(a,b)，返回计算结果
        # 否则通过logging记录错误信息，并友好退出
        logging.warning('variable "a" and "b" cannot be added!')
        return
    return wrapper  # fn引用add函数对象，并被存在闭包的执行h环境中返回

@checkParams    # 等同于 add = checkParams(add)
def add1(a,b):
    return a+b

if __name__ == '__main__':
    # 将 add函数对象传入，fn指向add
    # 等号左侧的add,指向checkParams的返回值wrapper
    add = checkParams(add)
    add(3,'hello')  # 经过检查类型，不会计算结果，而是记录日志并退出
    #print add(3,5)
    print checkParams(add)(4,5)   # 也是可以的，感觉有点复杂而已，难理解
    print add1(5,8)