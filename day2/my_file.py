# -*- coding:utf-8 -*-
#read file

#f = open('test.txt')
#for line in f.readlines():
#    print line,
#f.close()

#write file
f = open('test.txt','w')
f.write('this is first line.\n')
f.write('this is second line.\n')
f.write('this is third line.\n')
f.close()

# append
f = open('test.txt','a')
f.write('this is the appending line.\n')
f.write('this is the appending line.\n')
f.close()

# read and write: r+ 读写  W+ 写读
f = open('test.txt','r+')
print f.readline()
print f.readline()
f.write('this is the R+ modle.\n')
f.flush()
for line in f.readlines():
    print line,
f.close()

#  文件操作：读取大文件时注意
#   read() 把这个文件读取到内存
#   for line in readlines():  读取文件转出列表，性能非常低
#   for line in xreadlines(): 每次读取1行 ，再存储到硬盘