# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 15:59:33 2021

@author: bhs89
"""

import sys
import os
import datetime
from datetime import datetime as dt
import time
import random as rd

print(sys.path)

print(os.listdir(os.getcwd()))

print(__file__)
 
print(datetime.datetime.now())
print(dir(datetime))
print(dt.now().year)

today = dt.today()
print('오늘은 {}년 {}월 {}일입니다.'.format(today.year, today.month,today.day))
print(today.strftime('%Y-%m-%d %H:%M:%S'))
xMas = dt(2021,12,25)
print(xMas)

count = xMas - today

print('크리스마스까지 {}일 남았습니다.'.format(count.days)) 

print(datetime.datetime.now()+datetime.timedelta(days = 100))

time.sleep(1)
print("짠")

List = [1,2,3,4,5]
rd.shuffle(List)
print(List)
print(rd.choice(List))
print(rd.sample(List, 3))

# 11/23 practice
# def calc():
#     try :
#         a,b = input("두 수를 입력하세요 : ").split()
#         result = int(a) / int (b)
#     except Exception as er:
#         print("다시 입력하세요.",er)
#         calc()
#     else :
#         print("{} / {} = {}".format(a,b,result))
#     finally :
#         print("어쨋든 실행")

# #main
# calc()

# a = int(input("1~5 사이 수 입력 : "))
# assert 1<a<5, "에러 발생"

# 11/24 pracitce
# import os

# print("hi")
# os.path.abspath('.')
# os.getcwd()
# os.chdir("C:/Users/bhs89/OneDrive/바탕 화면/광운대학교/자료구조")
# print(os.getcwd())
# os.chdir("C:/Users/bhs89/OneDrive/바탕 화면/광운대학교/자료구조/3차과제")
# print(os.getcwd())

# f = open('test.txt','w')

# for i in range(5):
#    n = input("정수 입력하세요 : ")
#    f.write(n)
#    f.write("\n")
  
# f.close()

# h = open('test.txt','a')
# h.write("한글 세종대왕 만세")
# h.close()


# g = open('test.txt','r',encoding='utf-8')
# # sum = 0
# # ave = 0 
# for j in range(6):
#     s = g.readline()
#     print(s)
# #     sum += int(s)
    
# # print(sum)
# # print(sum/5)
# # g.close()    

# # h = open('test.txt','a+')
# # h.write("한글 세종대왕 만세")
# # for j in range():
# #     s = h.readline()
# #     print(s)
# # h.close()

# # i = open('test.txt','rt',encoding='utf-8')
# # for j in range(5):
# #     s = i.readline()
# #     print(s)
# # i.close()