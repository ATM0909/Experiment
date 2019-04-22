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
        self.setWindowTitle("方程求根")
        self.setGeometry(200, 200, 640, 400)
        m = Interpolation(self, width=5, height=4)#实例化一个画布对象
        m.move(0, 0)
        #设置原始图像按钮
        button = QPushButton('原始图', self)
        button.move(520, 20)
        button.resize(100, 75)
        button.clicked.connect(m.drawfunc)

        #设置二分法按钮
        button = QPushButton('二分法', self)
        button.move(520, 115)
        button.resize(100, 75)
        button.clicked.connect(m.drawdichotomy)

        #设置牛顿法按钮
        button = QPushButton('牛顿法', self)
        button.move(520, 210)
        button.resize(100, 75)
        button.clicked.connect(m.drawNewton)

        #设置弦截法按钮
        button = QPushButton('弦截法', self)
        button.move(520, 305)
        button.resize(100, 75)
        button.clicked.connect(m.secant)
        self.show()

#方程求根类
class Interpolation(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        #初始化各项值
        self.a=0.0001
        self.a0=2.5
        self.b=3
        self.eps=0.00001 #精度
        self.x0=3 #牛顿法近似值
        #原始函数的值
        self.x=np.linspace(0,3.5)
        self.y=[self.func(i) for i in self.x]
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
         #挪动坐标位置
        self.axes.set_xlim(0,4.5)
        #去掉边框
        self.axes.spines['top'].set_color('none')
        self.axes.spines['right'].set_color('none')
        #移位置 设为原点相交
        self.axes.xaxis.set_ticks_position('bottom')
        self.axes.spines['bottom'].set_position(('data',0))
        self.axes.yaxis.set_ticks_position('left')
        self.axes.spines['left'].set_position(('data',0))
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        #初始图像
        #self.main()

    #原始函数
    def func(self,x):
        return x-2*np.sin(x)

    def f(self,x):
        return 1-2*np.cos(x)

    #绘制原始图像
    def drawfunc(self):
        #绘图
        self.axes.plot(self.x,self.y,c='red',label="原始图像")
        self.axes.legend(loc=4)#指定legend的位置右下角
        self.draw()

    #绘制二分法图像
    def drawdichotomy(self):
        c=[(self.a+ self.b)/2.0]
        if(self.func( self.a)* self.func( self.b)<0):
            while(abs(self.a-self.b)> self.eps):
                c.append((self.a+self.b)/2.0)
                if(abs( self.func(c[-1]))<self.eps):
                    break
                elif((self.func(self.a)*self.func(c[-1]))<0):
                    self.b=c[-1]
                elif((self.func(self.b)*self.func(c[-1]))<0):
                    self.a=c[-1]
        else:
            return 0
        #return c,c[-1]
        #绘图
        for i in c:
            self.axes.plot([i,i],[0,self.func(i)])
         #积分结果
        self.axes.text(0.25,4,"二分法求值为：{}".format(c[-1])+" 共二分{}".format(len(c)-1)+"次")
        self.draw()

    #绘制牛顿法图像
    def drawNewton(self):
        count=0
        while abs(self.func(self.x0))>self.eps:
            x1=self.x0-self.func(self.x0)/self.f(self.x0)
            count=count+1
            self.axes.plot([self.x0,self.x0],[0, self.func(self.x0)],ls=':')
            self.axes.plot([self.x0 ,x1],[self.func(self.x0),0])
            self.x0=x1
         #积分结果
        self.axes.text(0.25,3.75,"牛顿法求值为：{}".format(self.x0)+" 共迭代{}".format(count)+"次")
        self.draw()

    #弦截法
    def secant(self):
        x=[self.a0, self.b]
        count=0
        while(abs(x[-1]-x[-2])>= self.eps):
            c=x[-1]- self.func(x[-1])*(x[-1]-x[-2])/( self.func(x[-1])- self.func(x[-2]))
            x.append(c)
            count=count+1
            self.axes.plot([x[-3],x[-3]],[0,  self.func(x[-3])],ls=':')
            self.axes.plot([x[-3],x[-1]],[ self.func(x[-3]),0])
        self.axes.text(0.25,3.5,"弦截法求值为：{}".format(x[-1])+" 共迭代{}".format(count)+"次")
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
