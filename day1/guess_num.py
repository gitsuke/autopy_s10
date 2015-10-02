# -*- coding:utf-8 -*-
import random

real_num = random.randrange(10)
retry_count = 0
while retry_count < 3:
#for i in range(3):
    guess_num = raw_input('please guess the real number:').strip()
    if len(guess_num)  == 0:
        continue
    if guess_num.isdigit():
        guess_num = int(guess_num )
    else:
        print 'Please input a number!'
        continue
    if guess_num > real_num :
        print 'Wrong! you need  try smaller!'
    elif guess_num < real_num :
        print 'Wrong! you need  try bigger!'
    else:
        print 'Congratulation! you got it.'
        break
    retry_count +=1
else:
    print 'The real num is ', real_num