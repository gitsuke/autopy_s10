# -*- coding:utf-8 -*-
'''
user_dict = {'test':{'passwd':'test','flag':'unlock'},
             'user':{'passwd':'user','flag':'unlock'}}
if (user_dict.get('test') and
        user_dict['test']['passwd'] == 'test' and
        user_dict['test']['flag'] == 'unlock'):
    print 'login'
'''
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
'''
import cPickle as pickle
with open('city_account.pkl') as f:  #载入用户账户密码信息
    city_dict = pickle.load(f)

city_list = []  # dict -> str list format
for key_shi in city_dict:
    for key_qu in city_dict[key_shi]:
        for key_di in city_dict[key_shi][key_qu]:
            citye_str = key_shi + ' ' + key_qu + ' ' + key_di + ' ' + str(city_dict[key_shi][key_qu][key_di])
            city_list.append(citye_str)
for i in city_list:
    print i
'''
import cPickle as pickle
with open('city_account.pkl') as f:  #载入城市信息
    city_dict = pickle.load(f)
return_flag = False
while True:
    del_city = raw_input('Please input deleting the Qu of city name: ').strip()
    if del_city == '':continue
    if del_city in city_dict:
        for key_qu in city_dict[del_city]:   #打印出该城市的所有区、县、镇
            print key_qu
        while True:
            del_qu = raw_input('Please input deleting the Qu: ').strip()
            if del_qu == '':continue
            elif del_qu in city_dict[del_city]:
                print city_dict[del_city][del_qu]
                #del city_dict[del_city][del_qu]
            else:
                print 'The key is incorrect,try again!'
            while True:
                del_ask = raw_input('Do you continue Delete or Return to main menu?(yes/no) ').strip()
                if del_ask == '':continue
                elif del_ask == 'yes':break
                elif del_ask == 'no':
                    return_flag = True
                    break
                else:
                    print 'Please input "yes" or "no",try again.'
                    continue
            if return_flag:break    #返回到上一级菜单
    else:
        print 'The input is incorrect,try again!'
        continue
    if return_flag:break    #返回到上一级菜单
print 'bye bye'