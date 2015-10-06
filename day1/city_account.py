# -*- coding:utf-8 -*-
import cPickle as pickle
while True:
    username = raw_input('please input your name: ').strip()
    passwd = raw_input('please input your passwd: ').strip()
    if username == 'admin' and passwd == 'admin':
       break
    else:
        print 'username or passwd is incorrect,try again!'
        continue
city_dict = {'guangZhou':{'tianHeQu':{'tianHeTiYuGuan':{'addr':'tianHeLu','tel':'020-86231236'},
                                    'jinSanDaXia':{'addr':'wuShanLu','tel':'020-86211254'}},
                          'yueXiuQu':{'yueXiuGongYuan':{'addr':'yueXiuLu','tel':'020-86195147'},
                                    'guangXiaoSi':{'addr':'guangXiaoLu','tel':'020-86214521'}},
                          'panYuQu':{'chongLong':{'addr':'yingBingLu','tel':'020-86198888'},
                                    'daFuShan':{'addr':'zhongCun','tel':'020-86652358'}}},

             'shenZhen':{'fuTianQu':{'lianHuaShan':{'addr':'lianHuaLu','tel':'0755-56871236'},
                                    'saiGe':{'addr':'shenNanZhongLu','tel':'0755-56878888'}},
                          'longGangQu':{'yuanShanGongYuan':{'addr':'yuanShanLu','tel':'0755-56231478'},
                                    'longChengGuangChang':{'addr':'longChengLu','tel':'0755-56984521'}},
                          'nanShanQu':{'shiJieZhiChuang':{'addr':'huaQiaoCheng','tel':'0755-54718888'},
                                    'huanLeGu':{'addr':'duJuanShan','tel':'0755-56874652'}}},

             'foShan':{'chanChengQu':{'liangYuan':{'addr':'songFengLu','tel':'0757-85236987'},
                                    'kongMiao':{'addr':'zuMiaoLu','tel':'0757-85235478'}},
                          'nanHaiQu':{'qianDengHu':{'addr':'dengHuXiLu','tel':'0757-85233698'},
                                    'gangGongYuan':{'addr':'gangShanLu','tel':'0757-85235410'}},
                          'shunDeQu':{'qingHuiYuan':{'addr':'qingHuiLu','tel':'0757-85231452'},
                                    'xiShanMiao':{'addr':'xiShanLu','tel':'0757-85233212'}}}}
with open('city_account.pkl','w') as f:
    pickle.dump(city_dict, f)