# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 14:34:06 2021

@author: bhs89
"""
import turtle
import random

turtle.clearscreen()

tt = turtle.Turtle()
scr = turtle.Screen()

image1 = 'muji.gif'
image2 = 'brown-line.gif'
image3 = 'kakao_lion.gif'
scr.addshape(image1)
scr.addshape(image2)
scr.addshape(image3)


t1 = turtle.Turtle()
t1.shape(image1)
t1.penup()
t1.goto(-300,300)
t1.pendown()

t2 = turtle.Turtle()
t2.shape(image2)
t2.penup()
t2.goto(-300,0)
t2.pendown()

t3 = turtle.Turtle()
t3.shape(image3)
t3.penup()
t3.goto(-300,-300)
t3.pendown()

for i in range(100):
    speed1 = random.randint(1, 10)
    t1.forward(speed1)
    speed2 = random.randint(1, 10)
    t2.forward(speed2)
    speed3 = random.randint(1, 10)
    t3.forward(speed3)

turtle.done()