# -*- coding:utf-8 -*-

user_dict = {'test':{'passwd':'test','flag':'unlock'},
             'user':{'passwd':'user','flag':'unlock'}}
if (user_dict.get('test') and
        user_dict['test']['passwd'] == 'test' and
        user_dict['test']['flag'] == 'unlock'):
    print 'login'
'''
import cPickle as pickle
count_lock = 0
with open('account.pkl') as f:  #载入用户账户密码信息
    user_dict = pickle.load(f)
while True:
    if count_lock == 5:   #5次出错，锁定账号
        with open('account.pkl','w') as f:
            for key in user_dict:
                user_dict[key]['flag'] = 'lock'
            print user_dict
            user_dict = pickle.dump(user_dict, f)
        print 'All users are locked, please contact your administrator to unlock.'
        break
    if count_lock < 5:
        count_lock += 1
        print count_lock

with open('account.pkl') as f:
    user_dict = pickle.load(f)
print user_dict
'''