# -*- coding:utf-8 -*-
# Author: suke
# At 2015/10/22 21:19

# name = 'python outsite'
#
# def info(a,b=5,c=10):
#     #name = 'suke'
#     print name
#     #name = 'suke haha'
#     print 'a is',a,', b is',b,', c is',c

# info(2,45)
# info(a=44,c=45)
# info(c=22,a=43)

# def info2(*args):
#     print args
# info2('suke',20,'IT')
#
# def info3(**args):
#     print args
#     if args['name2'] =='suke':
#         print 'Hi,',args['name2']
#         return args
#     else:
#         print 'good bye!'
#         return args
#
# d = info3(name2='suke1',age=20,job='IT')
# print d['name2']
'''
def f(x):
    return x**2
print f(3)

g = lambda x:x**2   #匿名函数
print g(3)  #跟 f(3)效果一样的

print map(f,range(10))

print map(lambda x:x**3,range(10))

dic1 = {
    2:3,
    4:6,
    9:9,
    'a':'as',
    '*':'$',
    'e':'tt'
}
print dic1.items()

# sorted(...)
#     sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
print sorted(dic1.items(),key=lambda x:x[0])
print sorted(dic1.items(),key=lambda x:x[1])
'''

#迭代器 iterator
import time
def run(n):
    '''
    print 'test 1'
    yield 1
    time.sleep(1)
    print 'test 2'
    time.sleep(1)
    print 'test 3'
    time.sleep(1)
    print 'test 4'
    time.sleep(1)
    print 'test 5'
    '''
    for i in range(n):
        print '---->',i
        yield i # 有yield语句的函数会被编译成生成器 constructor
        #print '---- do sth else ----'

#print type(run())   #变成迭代器

for j in run(10):
    #print j
    print 'return ',j,'** 3 =',j**3
    print '**** run',j+1,'times end ****'

print globals()
print locals()
print vars()
