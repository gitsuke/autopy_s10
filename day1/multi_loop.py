# -*- coding:utf-8 -*-

passwd = 'test'
logou_flag = False
for i in range(3):
    user_input = raw_input('Please input your passwd: ').strip()
    if len(user_input) == 0:continut
    if user_input  == passwd:
        while True:
            print 'Welcome login!'
            user_chiose = raw_input('''
            1. run a cmd
            2. send a file
            3. exit this level
            4. exit the whole system
            ''').strip()
            user_chiose = int(user_chiose )
            if user_chiose == 1:
                print 'going to a cmd'
            if user_chiose == 2:
                print 'going to send a file'
            if user_chiose == 3:
                print 'going to exit this level'
                break
            if user_chiose == 4:
                logout_flag = True
                break
    if logout_flag:
        print 'going to logout'
        break
