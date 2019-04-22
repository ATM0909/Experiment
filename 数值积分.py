import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

#显示中文和负数
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("数值积分")
        self.setGeometry(200, 50, 800, 600)
        m = Integration(self, width=7, height=6)#实例化一个画布对象
        m.move(0, 0)

        #设置龙贝格按钮
        button = QPushButton('龙贝格算法', self)
        button.move(700, 75)
        button.resize(100, 75)
        button.clicked.connect(m.Romberg1)

        #设置变步长积分按钮
        button = QPushButton('变步长积分', self)
        button.move(700, 450)
        button.resize(100, 75)
        button.clicked.connect(m.trap1)
        self.show()

#数值积分类
class Integration(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100 ):
        fig = Figure(figsize=(width, height), dpi=dpi ,frameon=False)
        self.axes=[]
        self.axes1 = fig.add_subplot(211)
        self.axes2 = fig.add_subplot(212)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.a=0
        self.b=6
        self.eps=0.0001
        #挪动坐标位置
        self.axes1.set_xlim(0,6)
        self.axes2.set_xlim(0,6)
        #去掉边框
        self.axes1.spines['top'].set_color('none')
        self.axes1.spines['right'].set_color('none')
        #移位置 设为原点相交
        self.axes1.xaxis.set_ticks_position('bottom')
        self.axes1.spines['bottom'].set_position(('data',0))
        self.axes1.yaxis.set_ticks_position('left')
        self.axes1.spines['left'].set_position(('data',0))
        #去掉边框
        self.axes2.spines['top'].set_color('none')
        self.axes2.spines['right'].set_color('none')
        #移位置 设为原点相交
        self.axes2.xaxis.set_ticks_position('bottom')
        self.axes2.spines['bottom'].set_position(('data',0))
        self.axes2.yaxis.set_ticks_position('left')
        self.axes2.spines['left'].set_position(('data',0))
        #初始为画图
        self.x=np.linspace(0,6)
        self.y=[self.func(i) for i in self.x]
        #self.Romberg1()

    #被积函数
    def func(self,x):
        if(x==0.0):
            return 1.0
        return np.sin(x)/x

    def getS(self,h):
        res=0
        for i in np.arange(self.a+h/2.0,self.b,h):
            res+=self.func(i)
        return res

    #变步长梯形公式
    def trap(self):
        h=self.b-self.a
        T=[]
        T.append(h * (self.func(self.a) + self.func(self.b)) /2.0)
        Tk=0
        c=[]
        while(1):
            Tk+=1
            s=self.getS(h)
            for i in np.arange(self.a+h/2.0,self.b,h):
                c.append(i-3+h*Tk)
            T.append((T[-1]+h*s)/2.0)
            if(abs(T[-1]-T[-2])<self.eps):
                break
            h/=2.0
        return (c,T[-1])
    #龙贝格算法积分
    def Romberg(self):
        k=1
        T=[]            # 复化梯形序列
        S=[0]            # Simpson序列
        C=[0]            # Cotes序列
        R=[]            # Romberg序列
        h = self.b - self.a
        T.append(h * (self.func(self.a) + self.func(self.b)) / 2.0)
        counter =0
        Rk=0
        c=[]
        while(1):
            Rk+=1
            counter+=1
            s=self.getS(h)
            T.append((T[-1]+h*s)/2.0)
            S.append((4.0*T[-1]-T[-2])/3.0)
            h/=2.0
            if(k==1):
                k+=1
            C.append((16.0*S[-1]-S[-2])/15.0)
            if(k==2):
                k+=1
            R.append((64.0*C[-1]-C[-2])/63.0)
            if(k==3):
                k+=1
            elif(abs(R[-1]-R[-2])<self.eps or counter>=100):
                break
        for i in range(1,2**Rk):
            c.append(self.a+i*(self.b-self.a)/2**Rk)
        return (c,R[-1])

    #绘制龙贝格图像
    def Romberg1(self):
        self.axes1.plot(self.x,self.y,'black',label='函数图像')
        self.axes1.legend()#默认legend在右上方
        x,y=self.Romberg()
        #积分结果
        self.axes1.text(3,0.5,"积分值是：{}".format(y))
        for i in x:
            self.axes1.plot([i,i],[0,self.func(i)], color = 'red' ,linestyle="--")
        self.draw()

    #绘制变步长梯形
    def trap1(self):
        self.axes2.plot(self.x,self.y,'black',label='函数图像')
        self.axes2.legend()#默认legend在右上方
        x,y=self.trap()
        self.axes2.text(3,0.5,"积分值是：{}".format(y))#积分结果
        for i in x:
            self.axes2.plot([i,i],[0,self.func(i)], color = 'green' ,linestyle="--")
        self.draw()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())