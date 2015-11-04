# -*- coding:utf-8 -*-
# Author: suke
# At 2015/10/25 13:57

import time
import pickle
import json

f = open('data.pkl')
jf = open('json.txt')
dit1 = pickle.load(f)
json1 = json.load(jf)
print dit1
print json