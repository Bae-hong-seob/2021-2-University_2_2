# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 16:07:49 2021

@author: bhs89
"""

import turtle

turtle.clearscreen()

t1 = turtle.Turtle()
name_x = -200
name_y = -50

t1.penup()
t1.goto(name_x+0,name_y+50) # ㅂ
t1.pendown()
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

turtle.done()