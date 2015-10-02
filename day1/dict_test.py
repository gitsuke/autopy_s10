# -*- coding:utf-8 -*-

data = {'name':'alex',
        'age':18,
        'job':'CEO',
        'salary':5555}
print '1.', data
data['info'] = 'beijing'
print '2.', data
del data['job']
print '3.',data
for key in data:
    print key,data[key]
print '4.',data.get('job')
for key,val in data.items():
    print key,val
print '5.', data.items()
