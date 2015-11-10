# -*- coding:utf-8 -*-
# Author: suke
# At 2015/11/10 16:29

def wrapper():
    alist = range(1,101)
    def lazy_sum():
        return reduce(lambda x, y : x+y, alist)
    return lazy_sum

lazy_sum = wrapper()    # wrapper() 返回的是lazy_sum函数对象

if __name__ == '__main__':
    print lazy_sum()  # 5050
    print wrapper()()  # 这种写法结果也正确，可读性差，不建议使用。
