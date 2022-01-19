# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 16:12:10 2021

@author: bhs89
"""

print("자동차의 속도(speed)를 입력하세요. (단위 : km/h) :")
speed = int(input())

if speed >= 100:
    print("고속")
    
elif speed >= 60:
    print("중속")

else:
    print("저속") 