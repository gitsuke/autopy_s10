user_dict = {'test':{'passwd':'test','flag':'unlock'},
             'user':{'passwd':'user','flag':'unlock'}}
if (user_dict.get('test') and
        user_dict['test']['passwd'] == 'test' and
        user_dict['test']['flag'] == 'unlock'):
    print 'login'