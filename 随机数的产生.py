import numpy as np
#产生随机数X1,X2为区间，X3为个数
def suiji(x1,x2,x3):
    random_list = []
    for i in range(x3):#随机数个数
         #随机数范围
         a = np.random.uniform(x1, x2)
         #设置随机数的精度
         random_list.append(round(a, 3))
    return  random_list
print(suiji(-20,20,10))