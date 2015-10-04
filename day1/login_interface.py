# -*- coding:utf-8 -*-
import cPickle as pickle
import random

exit_flag = False   #初始化锁定的状态为false
count_lock = 0
print 'Welcome to login system!'
print '****************************'
with open('account.pkl') as f:  #载入用户账户密码信息
    user_dict = pickle.load(f)
while True:
    if count_lock == 5:   #5次出错，锁定账号
        with open('account.pkl','w') as f:
            for key in user_dict:
                user_dict[key]['flag'] = 'lock'
            user_dict = pickle.dump(user_dict, f)
        print '******************************************************************'
        print 'All users are locked, please contact your administrator to unlock.'
        break

    user = raw_input('please input your user: ').strip()
    if user == '':continue
    passwd = raw_input('please input your passwd: ').strip()
    if  user_dict.get(user) and user_dict[user]['flag'] == 'lock':
        print 'The %s is lock, please contact your administrator to unlock.' % user
        break
    #判断输入的用户名是否被锁定，并验证密码
    if (user_dict.get(user) and
            user_dict[user]['flag'] == 'unlock' and
            user_dict[user]['passwd'] == passwd):
        while True:
            print '***********************************************'
            guess_choise = raw_input('Do you start playing guess numbr? (yes/no): ').strip()
            if guess_choise == '':continue
            elif guess_choise == 'yes':
                print 'The number range is 1 - 10.'
                real_num = random.randrange(1,11)
                retry_count = 0
                while retry_count < 3:  #有3次机会猜数字
                    guess_num = raw_input('please guess the real number: ').strip()
                    if guess_num == '':continue
                    if guess_num.isdigit():
                        guess_num = int(guess_num )
                        if guess_num > real_num :
                            print 'Wrong! you need try smaller!'
                        elif guess_num < real_num :
                            print 'Wrong! you need try bigger!'
                        else:
                            print 'Congratulation! you got it.'
                            break
                    else:
                        print 'Please input a number,try again!'
                        continue

                    retry_count +=1
                else:
                    print '---------------------------------'
                    print 'The real number is ', real_num

            elif guess_choise == 'no':
                exit_flag = True
                break
            else:
                print 'Please input "yes" or "no",try again.'
                continue

    if exit_flag:break
    else:
        count_lock += 1
        if (5 - count_lock):
            print 'The user or passwd is incorrect, you have %s times try again!' %  (5-count_lock)

print 'Bye bye!'