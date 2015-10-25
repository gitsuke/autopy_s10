# -*- coding:utf-8

all_str = set('0123456789.+-*/()')
while True:
    calc = raw_input('Please input a formula to calculate:\n>>>').strip()
    if set(calc).issubset(all_str):
        try:
            result = eval(calc)
        except:
            print 'Input incorrect,try again!'
            continue
        print 'Calculation results: ', result
    else:
        print 'Input incorrect,try again!'
        continue
    exit_flag = False
    while True:
        ask = raw_input('Do you continue calculate or exit?(yes/no) ').strip()
        if ask == '':continue
        elif ask == 'yes':break
        elif ask == 'no':
            exit_flag = True
            break
        else:
            print 'Please input "yes" or "no",try again.'
            continue
    if exit_flag:break
print 'good bye!'