{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "TclError",
     "evalue": "invalid command name \".!canvas\"",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTclError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-512e497b6894>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     63\u001b[0m     \u001b[0mdrawfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl5\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m \u001b[0;34m,\u001b[0m\u001b[0;36m0.8\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1.4\u001b[0m \u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m5\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m6\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m4.6\u001b[0m\u001b[0;34m)\u001b[0m   \u001b[0;31m#这里为了简便，所赋的各个椭圆a,b与实际偏差较大\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"__main__\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 65\u001b[0;31m     \u001b[0mmain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-1-512e497b6894>\u001b[0m in \u001b[0;36mmain\u001b[0;34m()\u001b[0m\n\u001b[1;32m     61\u001b[0m     \u001b[0mtl6\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcolor\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"red\"\u001b[0m\u001b[0;34m)\u001b[0m                                                                     \u001b[0;31m#画一个火红的大太阳！（并不）\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     62\u001b[0m     \u001b[0mtl6\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m30\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\"red\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 63\u001b[0;31m     \u001b[0mdrawfn\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtl\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl1\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl2\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl3\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mtl5\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;36m1\u001b[0m \u001b[0;34m,\u001b[0m\u001b[0;36m0.8\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m1.4\u001b[0m \u001b[0;34m,\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m3\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m5\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m4\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m6\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m4.6\u001b[0m\u001b[0;34m)\u001b[0m   \u001b[0;31m#这里为了简便，所赋的各个椭圆a,b与实际偏差较大\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     64\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0m__name__\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"__main__\"\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     65\u001b[0m     \u001b[0mmain\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-1-512e497b6894>\u001b[0m in \u001b[0;36mdrawfn\u001b[0;34m(tl, tl1, tl2, tl3, tl4, tl5, n, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6, b6)\u001b[0m\n\u001b[1;32m     36\u001b[0m         \u001b[0my5\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0mmath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcos\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mn\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     37\u001b[0m         \u001b[0mscaledX5\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscaledY5\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mx5\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m50\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my5\u001b[0m \u001b[0;34m*\u001b[0m \u001b[0;36m50\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 38\u001b[0;31m         \u001b[0mtl\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgoto\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma1\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mscaledX\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m30\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mb1\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mscaledY\u001b[0m\u001b[0;34m)\u001b[0m                                \u001b[0;31m#设置六个行星以焦点相同的轨迹进行椭圆运动\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     39\u001b[0m         \u001b[0mtl1\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgoto\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma2\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mscaledX1\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m71.4\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mb2\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mscaledY1\u001b[0m\u001b[0;34m)\u001b[0m                         \u001b[0;31m#减去的值是由下面所赋的值所决定的\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     40\u001b[0m         \u001b[0mtl2\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mgoto\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0ma3\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mscaledX2\u001b[0m\u001b[0;34m-\u001b[0m\u001b[0;36m111.8\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mb3\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mscaledY2\u001b[0m\u001b[0;34m)\u001b[0m                       \u001b[0;31m# 所减的值的算法是 50*(a**2-b**2)*0.5-30\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/Desktop/miniconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36mgoto\u001b[0;34m(self, x, y)\u001b[0m\n\u001b[1;32m   1774\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_goto\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mVec2D\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1775\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1776\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_goto\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mVec2D\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1777\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1778\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mhome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/Desktop/miniconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m_goto\u001b[0;34m(self, end)\u001b[0m\n\u001b[1;32m   3156\u001b[0m                       (self.currentLineItem,\n\u001b[1;32m   3157\u001b[0m                       \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrentLine\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3158\u001b[0;31m                       \u001b[0mscreen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_pointlist\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrentLineItem\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3159\u001b[0m                       self.items[:])\n\u001b[1;32m   3160\u001b[0m                       )\n",
      "\u001b[0;32m~/Desktop/miniconda3/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m_pointlist\u001b[0;34m(self, item)\u001b[0m\n\u001b[1;32m    753\u001b[0m         (9.9999999999999982, 0.0)]\n\u001b[1;32m    754\u001b[0m         >>> \"\"\"\n\u001b[0;32m--> 755\u001b[0;31m         \u001b[0mcl\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcv\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcoords\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mitem\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    756\u001b[0m         \u001b[0mpl\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcl\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m-\u001b[0m\u001b[0mcl\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcl\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m2\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    757\u001b[0m         \u001b[0;32mreturn\u001b[0m  \u001b[0mpl\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<string>\u001b[0m in \u001b[0;36mcoords\u001b[0;34m(self, *args, **kw)\u001b[0m\n",
      "\u001b[0;32m~/Desktop/miniconda3/lib/python3.7/tkinter/__init__.py\u001b[0m in \u001b[0;36mcoords\u001b[0;34m(self, *args)\u001b[0m\n\u001b[1;32m   2464\u001b[0m         return [self.tk.getdouble(x) for x in\n\u001b[1;32m   2465\u001b[0m                            self.tk.splitlist(\n\u001b[0;32m-> 2466\u001b[0;31m                    self.tk.call((self._w, 'coords') + args))]\n\u001b[0m\u001b[1;32m   2467\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_create\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mitemType\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;31m# Args: (val, val, ..., cnf={})\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2468\u001b[0m         \u001b[0;34m\"\"\"Internal function.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTclError\u001b[0m: invalid command name \".!canvas\""
     ]
    }
   ],
   "source": [
    "import turtle\n",
    "import math\n",
    "\n",
    "def setpoint(t,a,b,color):\n",
    "    t.penup()\n",
    "    t.shape(\"circle\")                #设置行星的形状是圆的\n",
    "    t.color(color)                    #设置行星及轨道的颜色\n",
    "    t.goto(a,b*(-50))               #设置起始位置\n",
    "    t.pendown()\n",
    "\n",
    "def drawfn(tl,tl1,tl2,tl3,tl4,tl5,n,a1,b1,a2,b2,a3,b3,a4,b4,a5,b5,a6,b6):\n",
    "    setpoint(tl,-30,b1,\"gray\")\n",
    "    setpoint(tl1,-71.4,b2,\"orange\")\n",
    "    setpoint(tl2,-111.8,b3,\"blue\")\n",
    "    setpoint(tl3,-132.3,b4,\"yellow\")\n",
    "    setpoint(tl4,-150,b5,\"brown\")\n",
    "    setpoint(tl5,-192.6,b6,\"sea green\")\n",
    "    while n>=0:\n",
    "        n=n+0.01\n",
    "        x=math.sin(6*n)                                                      # 过程中n前面所乘的数字是相对的角速度\n",
    "        y=-math.cos(6*n)                                                   # 为了简便，这里不妨设置角速度比例为6:5:4:3:2:1 \n",
    "        scaledX, scaledY = x * 50, y * 50                             # 所以与实际有所差异\n",
    "        x1=math.sin(5*n)\n",
    "        y1=-math.cos(5*n)\n",
    "        scaledX1, scaledY1 = x1 * 50, y1 * 50\n",
    "        x2=math.sin(4*n)\n",
    "        y2=-math.cos(4*n)\n",
    "        scaledX2, scaledY2 = x2 * 50, y2 * 50\n",
    "        x3=math.sin(3*n)\n",
    "        y3=-math.cos(3*n)\n",
    "        scaledX3, scaledY3 = x3 * 50, y3 * 50\n",
    "        x4=math.sin(2*n)\n",
    "        y4=-math.cos(2*n)\n",
    "        scaledX4, scaledY4 = x4 * 50, y4 * 50\n",
    "        x5=math.sin(n)\n",
    "        y5=-math.cos(n)\n",
    "        scaledX5, scaledY5 = x5 * 50, y5 * 50\n",
    "        tl.goto(a1*scaledX-30,b1*scaledY)                                #设置六个行星以焦点相同的轨迹进行椭圆运动\n",
    "        tl1.goto(a2*scaledX1-71.4,b2*scaledY1)                         #减去的值是由下面所赋的值所决定的\n",
    "        tl2.goto(a3*scaledX2-111.8,b3*scaledY2)                       # 所减的值的算法是 50*(a**2-b**2)*0.5-30\n",
    "        tl3.goto(a4*scaledX3-132.3,b4*scaledY3)                     #再减去的30是为了让焦点在(0,0)\n",
    "        tl4.goto(a5*scaledX4-150,b5*scaledY4)\n",
    "        tl5.goto(a6*scaledX5-192.6,b6*scaledY5)             \n",
    "    tl.penup()\n",
    "    tl1.penup()\n",
    "    tl2.penup()\n",
    "    tl3.penup()\n",
    "    tl4.penup()\n",
    "    tl5.penup()\n",
    "def main():\n",
    "    wn=turtle.Screen()\n",
    "    wn.bgcolor(\"black\")\n",
    "    wn.screensize(1200,800)\n",
    "    tl=turtle.Turtle()\n",
    "    tl1=turtle.Turtle()\n",
    "    tl2=turtle.Turtle()\n",
    "    tl3=turtle.Turtle()\n",
    "    tl4=turtle.Turtle()\n",
    "    tl5=turtle.Turtle()\n",
    "    tl6=turtle.Turtle()\n",
    "    tl6.color(\"red\")                                                                     #画一个火红的大太阳！（并不）\n",
    "    tl6.dot(30,\"red\")\n",
    "    drawfn(tl,tl1,tl2,tl3,tl4,tl5,0,1 ,0.8, 2, 1.4 ,3, 2, 4, 3, 5, 4, 6, 4.6)   #这里为了简便，所赋的各个椭圆a,b与实际偏差较大\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
