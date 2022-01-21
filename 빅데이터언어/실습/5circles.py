# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 22:22:38 2021

@author: bhs89
"""

import turtle

turtle.clearscreen()

tt = turtle.Turtle()

circle_list = [[-100,0,'green'],[0,0,'yellow'],[100,0,'red'],[-50,-50,'purple'],[50,-50,'blue']]

for x,y,z in circle_list:
    tt.penup()
    tt.goto(x,y)
    tt.color(z)
    tt.begin_fill()
    tt.circle(20)
    tt.end_fill()
    tt.pendown()

turtle.done()