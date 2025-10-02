
"""
import turtle
s=turtle.Turtle()
s.speed(1)
s.forward(100)
s.backward(50)
s.right(90)
s.dot()
s.forward(200)
s.home()
s.goto(50,50)
s.shape("circle")
s.left(750)
s.right(75)
s.forward(70)
s.right(70)
s.forward(110)
turtle.done()
"""
'''
import turtle
t=turtle.Turtle()
t.speed(1)
t.penup()
t.setpos(50,50)
t.pendown()
t.pensize(20)
t.pencolor("red")
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
t.backward(100)
t.right(90)
t.forward(100)
t.left(90)
t.forward(100)
turtle.done()
'''
'''
import turtle 
t=turtle.Turtle()
color=["red","white","violet"]

t.speed(0.5)
t.width(5)
turtle.bgcolor("black")
for j in range(10):
    for i in range(15):
        t.color([i/15,j/25,1])
        t.right(90)
        t.circle(200-j*4,90)
        t.left(90)
        t.circle(200-j*4,90)
        t.right(180)
        t.circle(50,24)
turtle.done()
'''
'''
import turtle
colors=["violet","blue","green","red","yellow"]
sketch=turtle.Turtle()
turtle.bgcolor("black")
for i in range(100):
    sketch.pencolor(colors[i%2])
    sketch.width(i/100 + 2)
    sketch.forward(i)
    sketch.left(59)
turtle.done()
'''
'''
import turtle
t=turtle.Turtle()
turtle.bgcolor("black")
t.speed(0.5)
t.pensize(20)
t.pencolor("gold")
t.forward(100)
t.backward(100)
t.right(90)
t.forward(150)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.penup()
t.goto(130,0)
t.pendown()
t.left(90)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.backward(100)
t.penup()
t.goto(260,0)
t.pendown()
t.left(90)
t.forward(150)
t.backward(150)
t.left(90)
t.forward(100)
t.right(90)
t.forward(75)
t.right(90)
t.forward(100)
t.left(145)
t.forward(120)
t.penup()
t.goto(390,0)
t.pendown()
t.left(35)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(150)
t.right(90)
t.forward(50)
t.backward(100)
turtle.done()
'''
'''
import turtle 
t=turtle.Turtle()
t.pencolor("gold")
t.speed(0.5)
t.pensize(20)
t.width(14)
turtle.bgcolor("black")
# c
for i in range(210):
    t.left(1)
    t.backward(1)
t.penup()
t.goto(0,0)
t.pendown()
t.right(205)
for b in range(30):
    t.right(1)
    t.forward(1)
# s
t.penup()
t.goto(65,-110)
t.left(10)
t.pendown()
t.circle(30, 190)
t.circle(-30, 190)

t.penup()
t.goto(125,10)
t.left(10)
t.pendown()
# K
t.right(85)
t.forward(120)
t.backward(60)
t.left(45)
t.forward(75)
t.backward(75)
t.left(90)
t.forward(75)
t.penup()
t.goto(-70,20)
t.pendown()
t.write("team")
turtle.done()

'''











































