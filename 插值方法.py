import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as spi

#显示中文和负数
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("插值方法")
        self.setGeometry(200, 200, 640, 400)

        m = Interpolation(self, width=5, height=4)#实例化一个画布对象
        m.move(0, 0)

        #设置随机数按钮
        button = QPushButton('随机数', self)
        button.setToolTip("产生5个随机数")
        button.move(520, 20)
        button.resize(100, 75)
        button.clicked.connect(m.main)

        #设置牛顿插值按钮
        button = QPushButton('牛顿插值', self)
        button.move(520, 115)
        button.resize(100, 75)
        button.clicked.connect(m.main1)

        #设置拉格朗日按钮
        button = QPushButton('拉格朗日插值', self)
        button.move(520, 210)
        button.resize(100, 75)
        button.clicked.connect(m.main2)

        #设置三次样条插值
        button = QPushButton('三次样条插值', self)
        button.move(520, 305)
        button.resize(100, 75)
        button.clicked.connect(m.main3)
        self.show()

#插值方法类
class Interpolation(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #初始为牛顿插值图像
        #self.main()
        self.X = sorted(self.suiji(-20,20,5))
        self.Y = sorted(self.suiji(-20,20,5))
    #牛顿插值函数
    def newton_interpolation(X,Y,init):
        sum=Y[0]
        temp=np.zeros((len(X),len(X)))

        #将第一行赋值
        for i in range(0,len(X)):
            temp[i,0]=Y[i]

        temp_sum=1.0
        for i in range(1,len(X)):
            #x的多项式
            temp_sum=temp_sum*(init-X[i-1])

            #计算均差
            for j in range(i,len(X)):
                temp[j,i]=(temp[j,i-1]-temp[j-1,i-1])/(X[j]-X[j-i])
            sum+=temp_sum*temp[i,i]
        return sum

    #拉格朗日插值函数
    def lagrange_interpolation(X,Y,init):
        sum=0.0
        for i in range(len(X)):
            temp=Y[i]
            for j in range(len(X)):
                if(j!=i):
                    temp=temp*((init-X[j])/(X[i]-X[j]))
            sum=sum+temp
        return sum

    #产生随机数X1,X2为区间，X3为个数
    def suiji(self,x1,x2,x3):
        random_list = []
        for i in range(x3):#随机数个数
             #随机数范围
             a = np.random.uniform(x1, x2)
             #设置随机数的精度
             random_list.append(round(a, 3))
        return  random_list

    #绘制随机点
    def main(self):

        #绘图
        self.axes.scatter(self.X,self.Y,c='red',label="随机数据")#红点表示随机数
        self.axes.legend(loc=4)#指定legend的位置右下角
        self.draw()

    #绘制牛顿图像
    def main1(self):

        #在最小值至最大值区间取1000点
        X_temp=np.linspace(np.min(self.X),np.max(self.X),1000,endpoint=True)
        Y_temp=[]

        for x in X_temp:
            Y_temp.append(Interpolation.newton_interpolation(self.X,self.Y,x))

        #绘图
        #self.axes.scatter(self.X,self.Y,label="原始数据")#蓝点表示原来的值
        self.axes.plot(X_temp,Y_temp,':',label='牛顿插值')#插值曲线
        self.axes.legend(loc=4)#指定legend的位置右下角
        self.draw()

    #绘制拉格朗日图像
    def main2(self):

        #在最小值至最大值区间取100
        X_temp=np.linspace(np.min(self.X),np.max(self.X),100,endpoint=True)
        Y_temp=[]

        for x in X_temp:
            Y_temp.append(Interpolation.lagrange_interpolation(self.X,self.Y,x))

        #绘图
        #self.axes.scatter(self.X,self.Y,label="原始数据")
        self.axes.plot(X_temp,Y_temp,':',label='拉格朗日插值')#插值曲线
        self.axes.legend(loc=4)#指定legend的位置右下角
        self.draw()

    #绘制三次插值图像
    def main3(self):

        t= spi.splrep(self.X,self.Y)
        for j in range(0, len(self.X) - 1):
            x0 = np.linspace(self.X[0], self.X[j + 1],100)
            y0=spi.splev(x0,t)
        ##作图
        self.axes.plot(x0,y0,label='三次样条插值')#插值曲线
        self.axes.legend(loc=4)#指定legend的位置右下角
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
