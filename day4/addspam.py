# -*- coding:utf-8 -*-
# Author: suke
# At 2015/11/10 17:18

def addspam(fn): # fn = useful
    def new(*args): # args=(a,b)
        print 'spam,spam,spam'
        print '*args -->',args
        return fn(*args)
    print type(new)
    return new

@addspam
def useful(a,b):
    print a**2+b**2

def useful1(a,b):
    print a**2+b**2
if __name__ == '__main__':
    useful(2,3)
    addspam(useful1)(20,30) # 等价于函数前加@addspam ，执行useful1(20,30)
