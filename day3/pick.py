# -*- coding:utf-8 -*-
# Author: suke
# At 2015/10/25 13:47

import datetime
import pickle
import json

#dic1 = {'a':1,'b':2,'c':3,'time':datetime.datetime.now()}
dic1 = {'a':1,'b':2,'c':3}

f = open('data.pkl','w')
jf = open('json.txt','w')
#print pickle.dumps(dic1)
pickle.dump(dic1,f)
json.dump(dic1,jf)
f.close()
