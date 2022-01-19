# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 22:07:31 2021

@author: bhs89
"""
import turtle as tr

# 화면 초기화
tr.clearscreen()

# 배경에 미로그림을 삽입
def makeMaze():
    scr = tr.Screen()
    scr.setup(1200, 900)
    scr.bgpic("다운로드.png")
    scr.update()
    
def makeTurtle():
    t = tr.Turtle()
    t.shape('turtle')
    t.pensize(5)
    t.pencolor('blue')    
    return t

def startline(t):
    t.penup()
    t.goto(-70,380)
    t.right(90)
    
def go_end_ling(t):
    t.pendown()
    t.write('Gogo!!!',font=15)
    t.forward(150)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(35)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(210)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(250)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.forward(230)
    t.right(90)
    t.forward(220)
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(360)
    t.right(90)
    t.forward(160)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(100)
    t.write('Finish!!!',font=15)
    
    
    
makeMaze()
t = makeTurtle()
startline(t)
go_end_ling(t)

tr.done()

'''import turtle as tt

#화면 초기화
tt.clearscreen()

#tt.bgcolor('red')

scr = tt.Screen()

image_name = 'maze.gif'

scr.setup(400,400)
scr.addshape(image_name)


t1 = tt.Turtle()
t2 = tt.Turtle()

t1.shape('turtle')
t1.forward(100)

t2.penup()
t2.goto(0,-100)
t2.pendown()
t2.forward(100)


tt.shape('turtle')
tt.forward(300)
tt.right(90)
tt.forward(100)
tt.penup()
tt.forward(100)
tt.pendown()
tt.forward(100)


tt.done()'''
