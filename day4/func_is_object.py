# -*- coding:utf-8 -*-
# Author: suke
# At 2015/11/4 16:29

def test():
    i = {0}
    def a():
        i.add(3)
        print locals()
        print i

    a()
    print i
#test()

# Python中，一切都是对象
# ****函数是第一类对象****
# 所谓第一类对象，意思是可以用标识符给对象命名，并且对象可以被当作数据处理，
# 例如赋值、作为参数传递给函数，或者作为返回值return 等
def func(a,b):
    return a+b

# 使用其他变量引用这个函数对象
add = func  # 这里 add=func=func()
print 'func=func(1,2) -->',func(1,2) # result 3
print 'add=func(10,20) -->',add(10,20) # result 3

def caller_func(f):
    return f(100,200) # 引用func(100,200)

# 函数对象func作为参数传递给caller_func函数，传参过程类似于一个赋值操作f=func；
# 于是func函数对象，被caller_func函数作用域中的局部变量f引用，f实际指向了函数func；
# 当执行return f(100, 200)的时候，相当于执行了return func(100, 200)；
# 因此输出结果为300

if __name__ == '__main__':
    # 将函数func的对象func、add，分别赋值给函数caller_func的形式参数f
    print 'f=func -->',caller_func(func) # caller_func形参 f=func
    print 'f=add -->',caller_func(add) # caller_func形参 f=add

# ****函数对象 vs 函数调用****
# 无论是把函数赋值给新的标识符，还是作为参数传递给新的函数，
# 针对的都是函数对象本身，而不是函数的调用。
def func1():
    return 'hello Python'

ref1 = func1
ref2 = func1()
print 'type(ref1) -->',type(ref1)   # <type 'function'>
print 'type(ref2) -->',type(ref2)   # <type 'str'>

# ****闭包&LEGB法则****
# 所谓闭包，就是将组成函数的语句和这些语句的执行环境打包在一起时，得到的对象