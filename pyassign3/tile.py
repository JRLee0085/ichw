#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def createlist1(m,n):
    list1=[["empty" for i in range(int(m))] for i in range(int(n))]
    return list1
#构建了一个二维的列表代表要铺砖的空间，empty代表未被铺，occupied代表被铺上

def findempty(n,list1):
    listfind=[]
    for i in range(n):
        if "empty" in list1[i]:
            listfind.append("0")
        else:
            listfind.append("1")
    if "0" in listfind:
        return "False"
    else:
        return "go on"
#制造了一个判断用已知个数的砖是不是无重复的铺满了这个空间（后面的算法可能会出现重复铺一块的情况，后面会有具体说明）

def countnumber(m,n,a,b):
    number=m*n/(a*b)
    if number!=int(number):
        return "False"
    else:
        return "True"
#判断能否用整数的砖铺满，如果能，计算出有几个

def createlist2(m):
    listjudge=[0 for i in range(int(m)+1)]
    return listjudge
#构建了一个开关一样的列表，0代表竖着铺这块砖，1代表横着铺，之所以加一是为了让全为1的那一组接下来做plus的时候有意义

def plus(x,listjudge):
    if listjudge[x]==2:
        listjudge[x]=0
        if x<len(listjudge):
            listjudge[x+1]=listjudge[x+1]+1
            plus(x+1,listjudge)
    else:
        pass
#使刚刚的“开关”列表为二进制，通过不断plus之后递归直到经历了所有组的情况（全0到全1），确保不会遗漏    

def putin(number,a,b,m,n,list1,listjudge,listfinal,n1,c,d):
    #这里递归和while循环都可以做，但while循环在这种方法下显得更明了一点（while循环可以更明了的表示铺完了所需砖数就停下来）
    while n1<int(number):
        if list1[c][d]=="empty":
            i1=0
            i2=0
        #找到一块还没铺的砖
            listlastbutone=[]
            if listjudge[n1]==0:
                if c+b<=n and d+a<=m:
                    for i1 in range(int(a)):
                        for i2 in range(int(b)):
                            list1[c+i2][d+i1]="occupied"
                            position=(c+i2)*m+(d+i1)+1
                            listlastbutone.append(position)
                    n1=n1+1
                else:
                    n1=number
                #如果能放的下就放，放不下就跳出进行下一组
            else:
                if c+a<=n and d+b<=m:
                    for i1 in range(int(b)):
                        for i2 in range(int(a)):
                            list1[c+i2][d+i1]="occupied"
                            position=(c+i2)*m+(d+i1)+1
                            listlastbutone.append(position)
                    n1=n1+1   
                else:
                    n1=number
                #如果能放的下就放，放不下就跳出进行下一组
                #这里就会存在一个小漏洞，因为最初定位的是一块空位置，考虑了能不能放下这块砖，
                #但没有考虑放下这块砖的位置是否已有在过程中被铺上的砖，就可能出现铺重
                #但毕竟要铺的砖数是一定的，如果出现上述情况就必然会有空位置没铺
                #于是最前面又定义了一个函数排除了这种错误
            listlastbutone.sort()
            if listlastbutone!=[]:
                listfinal.append(listlastbutone)           
        else:
            c=c+1
            if c==n:
                c=0
                d=d+1
            else:
                d=d
        #找到下一个空位点
    return listfinal

def main():
    m,n=map(int,input().split())
    a,b=map(int,input().split())
    number=m*n/(a*b)
    if countnumber(m,n,a,b)=="False":
        print("no can do")
    else :
        listjudge=createlist2(number)
        listresult=[]
        for i in range(int(2**number)):
            listfinal=[]
            list1=createlist1(m,n)
            n1=0
            c,d=0,0
            putin(number,a,b,m,n,list1,listjudge,listfinal,n1,c,d)
            if findempty(n,list1)=="go on" and listfinal not in listresult:
                listresult.append(listfinal)
            #排除了错误与重复的结果
            listjudge[0]=int(listjudge[0])+1
            plus(0,listjudge)
    if listresult==[]:
        print("no can do")
    else:
        print("available solution types:",len(listresult))
        print(listresult)
        thenumber=input("the number of the solution you wish to see:")

#下面做可视化：
    import turtle
    wn = turtle.Screen()
    li = turtle.Turtle()
    li.speed(8)
    li.penup()
    li.setx(-50*int(m)/2)                    #以50为单位标度所以以下所有系数均乘了50
    li.sety(-50*int(n)/2)                     #为了使整个空间关于原点对称所以让起点在这个位置
    li.pendown() 
    for i in range(int(m)):
        li.forward(50*(i+1))
        li.left(90)
        li.forward(50*int(n))
        li.left(90)
        li.forward(50*(i+1))
        li.left(90)
        li.forward(50*int(n))
        li.left(90)
    for i in range(int(n)):
        li.forward(50*int(m))
        li.left(90)
        li.forward(50*(i+1))
        li.left(90)
        li.forward(50*int(m))
        li.left(90)
        li.forward(50*(i+1))
        li.left(90)
    # 上面画出了要铺砖的空间
    listuse=listresult[int(thenumber)-1]
    li.pensize(10)
    li.speed(5)
    for i in range(len(listuse)):
        li.setheading(0)
        a1=max(listuse[i])
        b1=min(listuse[i])
        c1=b1//int(m)
        c2=b1%int(m)
        print(c1,c2)
        d1=a1//int(m)
        d2=a1%int(m)
        print(d1,d2)
        li.penup()
        if c2==0:
            li.forward(50*(int(m)-1))
            li.setheading(90)
            li.forward(50*(c1-1))
        else:
            li.forward(50*(c2-1))
            li.setheading(90)
            li.forward(50*c1)
        li.setheading(0)
        li.pendown()
        #判断最左下的砖的位置，并把这块砖的左下角定位为铺砖的起点
        if d2==0 and c2==0:
            li.forward(50)
            li.left(90)
            li.forward(50*(d1-c1+1))
            li.left(90)
            li.forward(50)
            li.left(90)
            li.forward(50*(d1-c1+1))
        elif d2==0 and c2!=0:
            li.forward(50*(int(m)-c2+1))
            li.left(90)
            li.forward(50*(d1-c1))
            li.left(90)
            li.forward(50*(int(m)-c2+1))
            li.left(90)
            li.forward(50*(d1-c1))
        else:
            li.forward(50*(d2-c2+1))
            li.left(90)
            li.forward(50*(d1-c1+1))
            li.left(90)
            li.forward(50*(d2-c2+1))
            li.left(90)
            li.forward(50*(d1-c1+1))
        #判断最右上角的砖的位置，并定位这块砖的右上角
        #这样从左下到右上就勾勒出了这块砖
        li.penup()
        li.setx(-50*int(m)/2)
        li.sety(-50*int(n)/2)                         #每次铺完都返回原点再重复按这个方法计算
        li.pendown() 
    turtle.done()   

if __name__ == "__main__":
    main()

