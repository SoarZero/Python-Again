#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

city_dict = {
    "北京":{
        "昌平":{
            "沙河": ["oldboy","test"],
            "天通苑" :["链家地产","我爱我家"],
        },
        "朝阳" :{
            "国贸" :["CICC","HP"],
            "望京" :{"奔驰","陌陌"},
            "东直门" :{"Advent","飞信"},
        },
        "海淀" : {

        }
    },
    "山东":{
        "德州":{

        },
        "青岛":{

        },
        "济南":{

        },
    },
    "广东" :{
        "东莞" :{

        },
        "佛山" :{

        },
        "常熟" :{

        },
    },
}

#退回标志位
exit_flag = False

while not exit_flag  :
    for count1 in city_dict:               #打印第一级key值  value
        print(count1,city_dict[count1])
    usr_choice1 = input("选择-进入二级菜单>>>")      #选择进入下一级
    for count2 in city_dict[usr_choice1]:               #打印二级菜单内容
        print("\t",count2,city_dict[usr_choice1][count2])
    print("按q退出，按b 退回")
    usr_choice2 = input("选择-进入三级菜单>>>")
    while not exit_flag :
        if usr_choice2 in city_dict[usr_choice1]:           #
            for count3 in city_dict[usr_choice1][usr_choice2]:
                print("\t\t",count3,city_dict[usr_choice1][usr_choice2][count3])
            print("按q退出，按b 退回")
            usr_choice3 = input("选择进入四级菜单>>>")
            while not exit_flag :
                if usr_choice3 in city_dict[usr_choice1][usr_choice2]:
                    for count4 in city_dict[usr_choice1][usr_choice2][usr_choice3] :
                        print("\t\t\t",count4)
                    print("按q退出，按b 退回")
                    usr_choice4 = input("最后一层，请按提示操作>>>")
                    if usr_choice4 == "b":
                        pass
                    elif usr_choice4 == 'q' :
                        exit_flag = True
                elif usr_choice3 == 'q' :
                    exit_flag = True
                elif usr_choice3 == 'b' :
                    break
        elif usr_choice2 == 'q':
            exit_flag = True
        elif usr_choice2 == 'b':
            break

