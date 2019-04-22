import math
import numpy as np
import matplotlib.pyplot as plt

#初始函数
def func(x):
    y=1/(2*math.e**x-x-1)
    return  y
#微分方程
def f(x,y):
    return (-y-x*y*y)

#直接欧拉法，初值，步长 两个参数
def euler(x0,h):
    y=[]
    y.append(func(x0))
    x=[0]
    n = 2/h
    for i in range(int(n+1)):
        x.append(x[-1]+h)
        y.append(y[-1]+h * f(x[i],y[i]))
    return (x,y)

#改进欧拉法 初值，步长 两个参数
def mproveeuler(x0,h):
    yp=[]
    yc=[]
    y=[]
    y.append(func(x0))
    x=[0]
    n = 2/h
    for i in range(int(n+1)):
        x.append(x[-1]+h)
        yp.append(y[-1]+h * f(x[i],y[i]))
        yc.append(y[-1]+h * f(x[i+1],yp[-1]))
        y.append((yp[-1]+yc[-1])/2)
    return (x,y)


x1=np.linspace(0,2)
y1=[func(i) for i in x1]

x2,y2=euler(0,0.1)
x3,y3=mproveeuler(0,0.1)

plt.plot(x2,y2,color='green')
plt.plot([4,4],[0,1])
plt.plot(x3,y3,color='blue')
plt.plot([3,3],[0,1])
plt.plot(x1,y1,color='black')
plt.show()