from random import choice
import matplotlib.pyplot as plt
import math


class RandomWalk():

    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=500):

        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            direction = choice(list(range(361)))
            distance = choice([1, 2])
            x_step = math.cos(direction) * distance
            y_step = math.sin(direction) * distance

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)


# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()
plt.plot(rw.x_values, rw.y_values, 'b')

# 突出起点和终点
plt.scatter(0, 0, c='yellow', edgecolors='none', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

#在足迹终点坐标上标记距离原点位置
d = round(math.sqrt(rw.x_values[-1]*rw.x_values[-1] + rw.y_values[-1]*rw.y_values[-1]))
plt.text(rw.x_values[-1], rw.y_values[-1], d)

plt.show()

