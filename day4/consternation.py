# -*- coding:utf-8 -*-
# Author: suke
# At 2015/11/4 21:26

def login(func):
    print 'running user authentication'
    user = raw_input('login: ').split()
    if user == 'alex':
        print '---welcome login---'
        print func
        return func

@login
def task1(name):
    print 'run task',name
    return name

def task2():
    print 'run task 2'

def task3():
    print 'run task 3'

task1('haha')
task2()
task3()

