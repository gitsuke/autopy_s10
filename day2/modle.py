# -*- coding:utf-8 -*-

from os import system,popen
import commands
import multiprocessing as multi
import os, sys
#res = system('dir')
#print '-->',res
res2 = popen('dir "G:\python"').read()
print res2

print multi.cpu_count()

print '-->',os.path
print '--->',sys.path

print u'中文测试'