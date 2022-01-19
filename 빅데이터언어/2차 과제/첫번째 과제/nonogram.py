# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 01:02:31 2021

@author: bhs89
"""

import turtle as tt

tt.clearscreen()

t1 = tt.Turtle()

box_size = 10 # 한 셀의 사이즈
start_x = -300
start_y = 300
x = -300 #시작 x좌표
y = 300 #시작 y좌표

def startline(t1):
    t1.penup()
    t1.goto(-300,300)
    t1.pendown()

def fillbox(t1):
    t1.speed(100)
    t1.begin_fill()
    t1.forward(box_size)
    t1.left(90)
    t1.forward(box_size)
    t1.left(90)
    t1.forward(box_size)
    t1.left(90)
    t1.forward(box_size)
    t1.left(90)
    t1.end_fill()
    
def unfillbox(t1):
    t1.speed(100)
    t1.penup()
    t1.forward(box_size)
    t1.left(90)
    t1.forward(box_size)
    t1.left(90)
    t1.forward(box_size)
    t1.left(90)
    t1.forward(box_size)
    t1.left(90)
    t1.pendown()
    
def recursion_box(n,x,y,size, color='black'):
    if n == 1:
        for i in range(size):
            t1.color(color)
            fillbox(t1)
            t1.penup()
            x = x + box_size # x좌표
            t1.goto(x,y)
            t1.pendown()
        return x
    elif n == 2:
        for i in range(size):
            t1.color(color)
            unfillbox(t1)
            t1.penup()
            x = x + box_size # x좌표
            t1.goto(x,y)
            t1.pendown()
        return x

def next_line(y):
    t1.penup()
    y = y-box_size
    t1.goto(start_x,y)
    t1.pendown()
    return y
#main 함수
startline(t1)

x = recursion_box(2,x,y,20)
x = recursion_box(1, x,y, 11)
x = recursion_box(2, x,y, 3)
x = recursion_box(1, x,y, 6) #첫줄완성

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,19)
x = recursion_box(1,x,y,2)
x = recursion_box(1,x,y,9,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,5)
x = recursion_box(2,x,y,2) #2줄 완성

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,17)
x = recursion_box(1,x,y,3)
x = recursion_box(1,x,y,8,'steelblue1')
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,5)
x = recursion_box(2,x,y,4) #3줄 완성

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,16)
x = recursion_box(1,x,y,2)
x = recursion_box(1,x,y,9,'yellow2')
x = recursion_box(1,x,y,3,'steelblue1')
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,6) #4줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,14)
x = recursion_box(1,x,y,11)
x = recursion_box(1,x,y,4,'yellow2')
x = recursion_box(1,x,y,2,'steelblue1')
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,5) #5줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,12)
x = recursion_box(1,x,y,11)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,3)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,2,'steelblue1')
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,5) # 6줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,12)
x = recursion_box(1,x,y,11)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,3)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,2,'steelblue1')
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,5) #7줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,11)
x = recursion_box(1,x,y,11)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,4)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,1,'steelblue1')
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,5) #8줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,11)
x = recursion_box(1,x,y,10)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,4)
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,2,'steelblue1')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,5) #9줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,10)
x = recursion_box(1,x,y,9)
x = recursion_box(2,x,y,5)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,4)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,1,'steelblue1')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,5) #10줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,10)
x = recursion_box(1,x,y,7)
x = recursion_box(2,x,y,9)
x = recursion_box(1,x,y,5)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,5) #11줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,10)
x = recursion_box(1,x,y,5)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,5)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,5) #12줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,10)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,5) #13줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,10)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,6) #14줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,15)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,6)
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,7) #15줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,11)
x = recursion_box(1,x,y,9)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,2,'red1')
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,8) #16줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,11)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,12)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,9) #17줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,11)
x = recursion_box(1,x,y,9)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,10) #18줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,15)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,5)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,12) #19줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,15)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,12) #20줄

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,16)
x = recursion_box(1,x,y,4)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,13) #21

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,19)
x = recursion_box(1,x,y,6)
x = recursion_box(2,x,y,15) #22

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,16)
x = recursion_box(1,x,y,4)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,5)
x = recursion_box(2,x,y,11) #23

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,14)
x = recursion_box(1,x,y,7)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,8)
x = recursion_box(2,x,y,9) #24

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,14)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,13)
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,8) #25

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,14)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,13)
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,8) #26

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,13)
x = recursion_box(1,x,y,2)
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,5)
x = recursion_box(1,x,y,2,'red1')
x = recursion_box(1,x,y,6)
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,7) #27

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,13)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,4)
x = recursion_box(1,x,y,4,'red1')
x = recursion_box(1,x,y,5)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,7) #28

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,13)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(1,x,y,7,'red1')
x = recursion_box(1,x,y,2)
x = recursion_box(1,x,y,4,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,6) #29

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,4)
x = recursion_box(2,x,y,6)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(1,x,y,6,'red1')
x = recursion_box(1,x,y,4)
x = recursion_box(1,x,y,4,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,6) #30

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,6)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,2)
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,4)
x = recursion_box(1,x,y,4,'red1')
x = recursion_box(1,x,y,6)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,5) #31

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,8)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,2)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,4) #32

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,4)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,2) 
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,4)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,4,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,4) #33

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(1,x,y,5)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,3,'yellow2')
x = recursion_box(1,x,y,8)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,5)
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,6) #34

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(1,x,y,5)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,3)
x = recursion_box(1,x,y,1)
x = recursion_box(1,x,y,2,'yellow2')
x = recursion_box(1,x,y,9)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,8)
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,2)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,1) #35

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(1,x,y,4)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,18)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,8)
x = recursion_box(1,x,y,1,'yellow2')
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,4) #36

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,3)
x = recursion_box(2,x,y,8)
x = recursion_box(1,x,y,9)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,9)
x = recursion_box(2,x,y,4)
x = recursion_box(1,x,y,1)
x = recursion_box(2,x,y,1) #37

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(1,x,y,7)
x = recursion_box(2,x,y,9)
x = recursion_box(1,x,y,8)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,8)
x = recursion_box(2,x,y,2)
x = recursion_box(1,x,y,4)
x = recursion_box(2,x,y,1) #38

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(1,x,y,6)
x = recursion_box(2,x,y,10)
x = recursion_box(1,x,y,9)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,10)
x = recursion_box(2,x,y,4) #39

y = next_line(y)
x = start_x #위치 초기화

x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,25)
x = recursion_box(2,x,y,1)
x = recursion_box(1,x,y,5)
x = recursion_box(2,x,y,8) #40

name_x = x-300
name_y = y-100

t1.penup()
t1.goto(name_x,name_y)
t1.pendown()

t1.goto(name_x+0,name_y+50) # ㅂ
t1.goto(name_x+0,name_y-50)
t1.goto(name_x+0,name_y+0)
t1.goto(name_x+100,name_y+0)
t1.goto(name_x+100,name_y+50)
t1.goto(name_x+100,name_y-50)
t1.goto(name_x+0,name_y-50)

t1.penup()
t1.goto(name_x+150,name_y+75)
t1.pendown()

t1.goto(name_x+150,name_y-75) #ㅐ
t1.goto(name_x+150,name_y+0)
t1.goto(name_x+200,name_y+0)
t1.goto(name_x+200,name_y+75)
t1.goto(name_x+200,name_y-75)

t1.penup()
t1.goto(name_x+300,name_y+100)
t1.pendown()

t1.dot(10)
t1.penup()
t1.goto(name_x+250,name_y+80)
t1.pendown()
t1.goto(name_x+350,name_y+80)
t1.penup()
t1.goto(name_x+300,name_y+10)
t1.pendown()
t1.circle(30) #ㅎ

t1.goto(name_x+300,name_y-10)
t1.goto(name_x+250,name_y-10)
t1.goto(name_x+350,name_y-10) # ㅗ

t1.penup()
t1.goto(name_x+300,name_y-100)
t1.pendown()
t1.circle(30) # ㅇ

t1.penup()
t1.goto(name_x+400,name_y+0)
t1.pendown()
t1.goto(name_x+450,name_y+75)
t1.goto(name_x+500,name_y+0) # ㅅ

t1.penup()
t1.goto(name_x+500,name_y+50)
t1.pendown()
t1.goto(name_x+550,name_y+50)
t1.goto(name_x+550,name_y+100)
t1.goto(name_x+550,name_y+0) #ㅓ

t1.penup()
t1.goto(name_x+450,name_y-25)
t1.pendown()
t1.goto(name_x+450,name_y-100)
t1.goto(name_x+450,name_y-50)
t1.goto(name_x+550,name_y-50)
t1.goto(name_x+550,name_y-25)
t1.goto(name_x+550,name_y-100)
t1.goto(name_x+450,name_y-100) #ㅂ

t1.penup()
t1.goto(name_x+500,name_y-150)
t1.write('2018204042 정보융합학부',True,"center",('',20)) 
t1.pendown()


tt.done()