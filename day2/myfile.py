# -*- utf-8-*-

# read
#f = open('dir.txt')
#for line in f.xreadlines():
#    print line,
#f.close()

#write
f = open('myfile.txt','w')
f.write('this is the first line\n')
f.write('this is the second line\n')
f.write('this is the third line\n')
f.close()

# append
f = open('myfile.txt','a')
f.write('this is the append line\n')
f.write('this is the append line.  test test read line\n')
f.close()

## r+ read write
## w+ write read
'''
f = open('myfile.txt','r+')
print 'first line: ',f.readline()
print 'second line: ',f.readline()
#f.write('change third line')  r+ not write
print f.tell()
f.close()

f = open('myfile.txt','w+')
print 'first line: ',f.readline()
print 'second line: ',f.readline()
f.write('change third line\n')  
#print f.tell()
f.close()
'''