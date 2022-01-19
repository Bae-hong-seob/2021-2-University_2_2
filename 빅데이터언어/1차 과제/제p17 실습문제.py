# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:49:04 2021

@author: bhs89
"""

print("과제를 내 손으로 끝마친다 (Y/N)")
answer = input()

if answer == 'N':
    print("과톱의 도움을 받는다 (Y/N)")
    answer == input()
    
    if answer == 'Y':
        print("야식을 먹을까?(Y/N)")
        answer == input()
        
        if answer == 'Y':
            print("배부르게 불태운다.")
        else:
            print("굶주리며 불태운다.")
    else:
        print("내일 배 끼고, 지금은 잔다.")
elif answer == "Y":
        print("야식을 먹을까?(Y/N)")
        answer == input()
        
        if answer == 'Y':
            print("배부르게 불태운다.")
        else:
            print("굶주리며 불태운다.")
else:
    print("잘못입력하셨습니다.")