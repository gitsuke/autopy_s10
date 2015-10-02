# -*- coding:utf-8 -*-
import cPickle as pickle
while True:
    username = raw_input('please input your name: ').strip()
    passwd = raw_input('please input your passwd: ').strip()
    if username == 'admin' and passwd == 'admin':
       break
    else:
        print 'username or passwd is incorrect,try again!'
        continue
user_dict = {'test':{'passwd':'test','flag':'unlock'},
             'user':{'passwd':'user','flag':'unlock'}}
with open('account.pkl','w') as f:
    pickle.dump(user_dict, f)