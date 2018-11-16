#!/usr/bin/env python
# coding: utf-8

# In[1]:

import turtle
import math

def setpoint(t,a,b,color):
    t.penup()
    t.shape("circle")               #设置行星的形状是圆的
    t.color(color)                  #设置行星及轨道的颜色
    t.goto(a,b*(-50))               #设置起始位置
    t.pendown()

def drawfn(tl,tl1,tl2,tl3,tl4,tl5,n,a1,b1,a2,b2,a3,b3,a4,b4,a5,b5,a6,b6):
    setpoint(tl,-30,b1,"gray")
    setpoint(tl1,-71.4,b2,"orange")
    setpoint(tl2,-111.8,b3,"blue")
    setpoint(tl3,-132.3,b4,"yellow")
    setpoint(tl4,-150,b5,"brown")
    setpoint(tl5,-192.6,b6,"sea green")
    while n>=0:
        n=n+0.01
        x=math.sin(6*n)                                   # 过程中n前面所乘的数字是相对的角速度
        y=-math.cos(6*n)                                  # 为了简便，这里不妨设置角速度比例为6:5:4:3:2:1
        scaledX, scaledY = x * 50, y * 50                 # 所以与实际有所差异
        x1=math.sin(5*n)
        y1=-math.cos(5*n)
        scaledX1, scaledY1 = x1 * 50, y1 * 50
        x2=math.sin(4*n)
        y2=-math.cos(4*n)
        scaledX2, scaledY2 = x2 * 50, y2 * 50
        x3=math.sin(3*n)
        y3=-math.cos(3*n)
        scaledX3, scaledY3 = x3 * 50, y3 * 50
        x4=math.sin(2*n)
        y4=-math.cos(2*n)
        scaledX4, scaledY4 = x4 * 50, y4 * 50
        x5=math.sin(n)
        y5=-math.cos(n)
        scaledX5, scaledY5 = x5 * 50, y5 * 50
        tl.goto(a1*scaledX-30,b1*scaledY)                        #设置六个行星以焦点相同的轨迹进行椭圆运动
        tl1.goto(a2*scaledX1-71.4,b2*scaledY1)                   #减去的值是由下面所赋的值所决定的
        tl2.goto(a3*scaledX2-111.8,b3*scaledY2)                  # 所减的值的算法是 50*(a**2-b**2)*0.5-30
        tl3.goto(a4*scaledX3-132.3,b4*scaledY3)                  #再减去的30是为了让焦点在(0,0)
        tl4.goto(a5*scaledX4-150,b5*scaledY4)
        tl5.goto(a6*scaledX5-192.6,b6*scaledY5)             
    tl.penup()
    tl1.penup()
    tl2.penup()
    tl3.penup()
    tl4.penup()
    tl5.penup()
def main():
    wn=turtle.Screen()
    wn.bgcolor("black")
    wn.screensize(1200,800)
    tl=turtle.Turtle()
    tl1=turtle.Turtle()
    tl2=turtle.Turtle()
    tl3=turtle.Turtle()
    tl4=turtle.Turtle()
    tl5=turtle.Turtle()
    tl6=turtle.Turtle()
    tl6.color("red")                                              #画一个火红的大太阳！（并不）
    tl6.dot(30,"red")
    drawfn(tl,tl1,tl2,tl3,tl4,tl5,0,1 ,0.8, 2, 1.4 ,3, 2, 4, 3, 5, 4, 6, 4.6)
    #这里为了简便，所赋的各个椭圆a,b与实际偏差较大
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




