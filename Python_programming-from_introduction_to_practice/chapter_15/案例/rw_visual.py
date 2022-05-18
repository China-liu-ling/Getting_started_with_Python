import matplotlib.pyplot as plt
from practice_15_5 import RandomWalk

#创建一个RandomWalk实例
rw = RandomWalk()
rw.fill_walk()

#设置样式
plt.style.use('classic')

#设置图形尺寸
plt.figure(figsize=(15, 10))

#绘制散点图
point_numbers = range(rw.num_points)
plt.scatter(rw.x_values, rw.y_values, s=10, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors=None, alpha=0.5)

#突出起点和终点
plt.scatter(0, 0, c='red', edgecolors=None, s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors=None, s=50)

#隐藏坐标轴
#plt.gca().get_xaxis().set_visible(False)
#plt.gca().get_yaxis().set_visible(False)

#显示图形
plt.show()