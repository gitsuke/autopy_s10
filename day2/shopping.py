#!/usr/bin/env python
# -*- coding:utf-8 -*-

while True:
    wage = raw_input('Please input you wage: ').strip()
    if wage.isdigit():
        wage = int(wage)
        break
    else:
        print 'Please input the number of wage,tyr again!'
        continue

goods = {'apple':5000,'bike':800,'telsa':60000,'coffee':35}
parce =[goods[key] for key in goods]
parce.sort()
total_number = 0
total_cost = 0
shopping_list = []
while True:
    print '''----------------------------------------\t
            apple\t %s\t
            bike\t  %s\t
            telsa\t %s\t
            coffee\t    %s\t
            exit\t
            ----------------------------------------\t''' % (goods['apple'], goods['bike'],
                                                 goods['telsa'], goods['coffee'])
    choice = raw_input('Please choose the goods from shopping list or exit: ')
    if choice in goods:
        if wage - total_cost >= goods[choice]:
            shopping_list.append(choice)
            total_cost += goods[choice]
        elif wage - total_cost >= parce[0]:
            print 'Your own %s YUAN, please choose other good or eixt.' % wage
        else:
            print 'Your own money can not pay for any goods,bye bye!'
            break
    elif choice == 'exit':
        break
    else:
        print 'Please choose the right goods,try again!'

goods_set = set(shopping_list)
print '''\t****************************************\t
        good\t   price\t    number\t    cost\t
        ----------------------------------------\t
        ''',
for i in goods_set:
    number = shopping_list.count(i)
    total_number += number
    cost = goods[i] * number
    print '%s    \t%s    \t%s    \t%s' % (i, goods[i], number, cost)
print '''\t****************************************\t
        All number: %s\t    All cost: %s\t
        ''' % (total_number, total_cost)
print 'Your rest money is %s.' % (wage-total_cost)
