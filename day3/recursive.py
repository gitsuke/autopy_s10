# -*- coding:utf-8 -*-
# Author: suke
# At 2015/10/26 19:57

def calc(n):
    print '-->',n
    if n/2 > 0:
        #calc(n/2)   # 打印******* 4次
        return calc(n/2)    # 打印******* 1次
    print '*******'
    return n
if __name__ == '__main__':
    print calc(12)