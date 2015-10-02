# -*- coding:utf-8 -*-
import cPickle as pickle

lock_flag = False   #初始化锁定的状态为false

while True:
    print '''Welcome to login system!
            1. login system
            2. exit system
            *************************'''
    get_input = raw_input('please input your choise number: ').strip()
    if get_input == '':continue
    elif get_input == '1':
        #载入用户账户密码信息
        with open('account.pkl') as f:
            user_dict = pickle.load(f)

        user = raw_input('please input your user: ').strip()
        if user == '':continue
        passwd = raw_input('please input your passwd: ').strip()
        if passwd == '':continue
        #判断输入的用户名与密码已经是否被锁定
        if (user_dict.get(user) and
                user_dict[user]['passwd'] == passwd and
                user_dict[user]['flag'] == 'unlock'):
            print 'Welcome %s to here:' % user

    elif get_input == '2':
        print 'good bye!'
        break
    else:
        print 'your chiose incorrect,try again!'
