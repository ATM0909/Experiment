import math
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x-2*np.sin(x)

x=np.linspace(0,3)
y=[func(i) for i in x]

plt.plot(x,y)
 #挪动坐标位置
ax=plt.gca()
ax.set_xlim(0,6)
ax.set_xlim(0,6)
#去掉边框
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
#移位置 设为原点相交
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()