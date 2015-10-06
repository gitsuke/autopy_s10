# -*- coding:utf-8 -*-
import cPickle as pickle

while True:
    with open('city_account.pkl') as f:  #载入城市信息
        city_dict = pickle.load(f)
    return_flag = False #初始化返回到主菜单标识
    print '''*** Welcome to city system! ***
            1. Query
            2. Add
            3. Delete
            4. Update
            5. Exit'''
    get_input = raw_input('Please choise the number: ').strip()
    if get_input =='':continue
    elif get_input == '1':
        city_list = []  # dict -> str list format
        for key_shi in city_dict:
            for key_qu in city_dict[key_shi]:
                for key_di in city_dict[key_shi][key_qu]:
                    citye_str = key_shi + ' ' + key_qu + ' ' + key_di + ' ' + str(city_dict[key_shi][key_qu][key_di])
                    city_list.append(citye_str)
        while True:
            query_count = 0 #记录输入的查询数据是否存在
            query_input = raw_input('Please input your quety info: ').strip()
            if query_input =='':continue
            for city in city_list:
                if query_input in city:
                    query_count += 1    #统计查询到的次数
                    print  city
            if query_count == 0:
                print 'Do not query your input info,try again!'
            while True:
                query_ask = raw_input('Do you continue Query or Return to main menu?(yes/no) ').strip()
                if query_ask == '':continue
                elif query_ask == 'yes':break
                elif query_ask == 'no':
                    return_flag = True
                    break
                else:
                    print 'Please input "yes" or "no",try again.'
                    continue
            if return_flag:break    #返回到主菜单

    elif get_input == '2':
        while True:
            add_city_info = ['chengShi','Qu/Xian/Zhen','addressName','Address','Telephone']
            add_count = 0 # city_info index
            add_city = []
            while True:
                add_input = raw_input('Please input add %s info: ' % add_city_info[add_count]).strip()
                if add_input == '':continue
                else:
                    add_city.append(add_input)
                    add_count += 1
                if add_count == 5:break #信息输入完后结束循环

            # 城市字典四层嵌套，从内到外逐层添加，最后完成新增信息
            add_chengShi = add_city[0]
            add_qu = add_city[1]
            add_addr_name = add_city[2]
            add_address = add_city[3]
            add_tel = add_city[4]
            city_dict[add_chengShi][add_qu][add_addr_name] = {'addr':add_address,'tel':add_tel}
            while True:
                add_ask = raw_input('Do you continue Add or Return to main menu?(yes/no) ').strip()
                if add_ask == '':continue
                elif add_ask == 'yes':break
                elif add_ask == 'no':
                    return_flag = True
                    break
                else:
                    print 'Please input "yes" or "no",try again.'
                    continue

            with open('city_account.pkl','w') as f:  #把新增的信息保存到文件中
                city_dict = pickle.dump(city_dict, f)
            if return_flag:break    #返回到主菜单

    elif get_input == '3':
        while True:
            print '''***********************************
                1. del City
                2. del Qu/Xian/Zhen
                3. del AddressName
                4. Return main menu'''

            del_index = raw_input('Please choise the number: ').strip()
            if del_index == '':continue
            elif del_index == '1':
                while True:
                    del_city = raw_input('Please input the city name: ').strip()
                    if del_city == '':continue
                    elif del_city in city_dict:
                        del city_dict[del_city]
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
                    with open('city_account.pkl','w') as f:  #把删除的信息保存到文件中
                        city_dict = pickle.dump(city_dict, f)
                    if return_flag:break    #返回到上一级菜单

            elif del_index == '2':
                while True:
                    del_city = raw_input('Please input the city name: ').strip()
                    if del_city == '':continue
                    elif del_city in city_dict:
                        for key_qu in city_dict[del_city]:
                            print key_qu,
                        while True:
                            del_qu = raw_input('\nPlease input the Qu name: ').strip()
                            if del_qu == '':continue
                            elif del_qu in city_dict[del_city]:
                                del city_dict[del_city][del_qu]
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

                    with open('city_account.pkl','w') as f:  #把删除的信息保存到文件中
                        city_dict = pickle.dump(city_dict, f)
                    if return_flag:break    #返回到上一级菜单

            elif del_index == '3':
                while True:
                    del_city = raw_input('Please input the city name: ').strip()
                    if del_city == '':continue
                    del_qu = raw_input('Please input the Qu name: ').strip()
                    if del_qu == '':continue
                    if del_city in city_dict and del_qu in city_dict[del_city]:
                        for key_addr in city_dict[del_city][del_qu]:
                           print key_addr,
                        while True:
                            del_addr_name = raw_input('\nPlease input the address name: ').strip()
                            if del_addr_name == '':continue
                            elif del_addr_name in city_dict[del_city][del_qu]:
                                del city_dict[del_city][del_qu][del_addr_name]
                            else:
                                print 'The key is incorrect,try again!'
                            while True:
                                del_ask = raw_input('Do you continue Delete or Return main menu?(yes/no) ').strip()
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
                    with open('city_account.pkl','w') as f:  #把删除的信息保存到文件中
                        city_dict = pickle.dump(city_dict, f)
                    if return_flag:break    #返回到上一级菜单

            elif del_index == '4':break

    elif get_input == '4':
        while True:
            print '''****************************************
                1. update Qu/Xian/Zhen
                2. update AddressName
                3. update Address
                4. update Telephone
                5. Return main menu'''
            update_index = raw_input('Please choise the number: ').strip()
            if update_index == '':continue
            elif update_index == '1':
                while True:
                    update_city = raw_input('Please input update the city name: ').strip()
                    if update_city == '':continue
                    old_qu = raw_input('Please input the old Qu/Xian/Zhen name: ').strip()
                    if old_qu == '':continue
                    #判断输入的 城市以及区是否存在
                    if update_city in city_dict and old_qu in city_dict[update_city]:
                        print '****  The city infomation  **** '
                        for key_addr_name in city_dict[update_city][old_qu]:
                            print update_city, old_qu, key_addr_name, str(city_dict[update_city][old_qu][key_addr_name])
                        while True:
                            update_qu = raw_input('Please input the update Qu/Xian/Zhen name: ').strip()
                            if update_qu == '':continue
                            update_value = city_dict[update_city][old_qu]   #先保存要更新区的数据
                            del city_dict[update_city][old_qu]  #删除要更新区的数据
                            city_dict[update_city][update_qu] = update_value    #赋予新的区名数据
                            while True:
                                update_ask = raw_input('Do you continue update or Return main menu?(yes/no) ').strip()
                                if update_ask == '':continue
                                elif update_ask == 'yes':break
                                elif update_ask == 'no':
                                    return_flag = True
                                    break
                                else:
                                    print 'Please input "yes" or "no",try again.'
                                    continue
                            if return_flag:break    #返回到上一级菜单
                    else:
                        print 'The input is incorrect,try again!'
                        continue
                    with open('city_account.pkl','w') as f:  #把删除的信息保存到文件中
                        city_dict = pickle.dump(city_dict, f)
                    if return_flag:break    #返回到上一级菜单

            elif update_index == '2':
                while True:
                    update_city = raw_input('Please input update city name: ').strip()
                    if update_city == '':continue
                    update_qu = raw_input('Please input update Qu/Xian/Zhen name: ').strip()
                    if update_qu == '':continue
                    if update_city in city_dict and update_qu in city_dict[update_city]:
                        print '****  The city infomation  **** '
                        for key_addr_name in city_dict[update_city][update_qu]:
                            print update_city, update_qu, key_addr_name, str(city_dict[update_city][update_qu][key_addr_name])
                    old_addr_name = raw_input('Please input the old address name: ').strip()
                    if old_addr_name == '':continue
                    #判断输入的 城市、区以及地名是否存在
                    if old_addr_name in city_dict[update_city][update_qu]:
                        while True:
                            update_addr_name = raw_input('Please input the update address name: ').strip()
                            if update_addr_name == '':continue
                            update_value = city_dict[update_city][update_qu][old_addr_name]   #先保存要更新地名的数据
                            del city_dict[update_city][update_qu][old_addr_name]  #删除要更新地名的数据
                            city_dict[update_city][update_qu][update_addr_name] = update_value    #赋予新的地名数据
                            while True:
                                update_ask = raw_input('Do you continue update or Return main menu?(yes/no) ').strip()
                                if update_ask == '':continue
                                elif update_ask == 'yes':break
                                elif update_ask == 'no':
                                    return_flag = True
                                    break
                                else:
                                    print 'Please input "yes" or "no",try again.'
                                    continue
                            if return_flag:break    #返回到上一级菜单
                    else:
                        print 'The input is incorrect,try again!'
                        continue
                    with open('city_account.pkl','w') as f:  #把删除的信息保存到文件中
                        city_dict = pickle.dump(city_dict, f)
                    if return_flag:break    #返回到上一级菜单

            elif update_index == '3':
                while True:
                    update_city = raw_input('Please input update city name: ').strip()
                    if update_city == '':continue
                    update_qu = raw_input('Please input update Qu/Xian/Zhen name: ').strip()
                    if update_qu == '':continue
                    if update_city in city_dict and update_qu in city_dict[update_city]:
                        print '****  The city infomation  **** '
                        for key_addr_name in city_dict[update_city][update_qu]:
                            print update_city, update_qu, key_addr_name, str(city_dict[update_city][update_qu][key_addr_name])
                    update_addr_name = raw_input('Please input update address name: ').strip()
                    if update_addr_name =='':continue
                    if update_addr_name in city_dict[update_city][update_qu]:
                        while True:
                            update_address = raw_input('Please input update address: ').strip()
                            if update_address == '':continue
                            else:
                                city_dict[update_city][update_qu][update_addr_name]['addr'] = update_address    #赋予新的地点数据
                            while True:
                                update_ask = raw_input('Do you continue update or Return main menu?(yes/no) ').strip()
                                if update_ask == '':continue
                                elif update_ask == 'yes':break
                                elif update_ask == 'no':
                                    return_flag = True
                                    break
                                else:
                                    print 'Please input "yes" or "no",try again.'
                                    continue
                            if return_flag:break    #返回到上一级菜单
                    else:
                        print 'The input is incorrect,try again!'
                        continue
                    with open('city_account.pkl','w') as f:  #把删除的信息保存到文件中
                        city_dict = pickle.dump(city_dict, f)
                    if return_flag:break    #返回到上一级菜单

            elif update_index == '4':
                while True:
                    update_city = raw_input('Please input update city name: ').strip()
                    if update_city == '':continue
                    update_qu = raw_input('Please input update Qu/Xian/Zhen name: ').strip()
                    if update_qu == '':continue
                    if update_city in city_dict and update_qu in city_dict[update_city]:
                        print '****  The city infomation  **** '
                        for key_addr_name in city_dict[update_city][update_qu]:
                            print update_city, update_qu, key_addr_name, str(city_dict[update_city][update_qu][key_addr_name])
                    update_addr_name = raw_input('Please input update address name: ').strip()
                    if update_addr_name =='':continue
                    if update_addr_name in city_dict[update_city][update_qu]:
                        while True:
                            update_address = raw_input('Please input update telephone: ').strip()
                            if update_address == '':continue
                            else:
                                city_dict[update_city][update_qu][update_addr_name]['tel'] = update_address    #赋予新的地点数据
                            while True:
                                update_ask = raw_input('Do you continue update or Return main menu?(yes/no) ').strip()
                                if update_ask == '':continue
                                elif update_ask == 'yes':break
                                elif update_ask == 'no':
                                    return_flag = True
                                    break
                                else:
                                    print 'Please input "yes" or "no",try again.'
                                    continue
                            if return_flag:break    #返回到上一级菜单
                    else:
                        print 'The input is incorrect,try again!'
                        continue
                    with open('city_account.pkl','w') as f:  #把删除的信息保存到文件中
                        city_dict = pickle.dump(city_dict, f)
                    if return_flag:break    #返回到上一级菜单

            elif update_index == '5': break
    elif get_input == '5':break

print '_*_ Good Bye! _*_'

