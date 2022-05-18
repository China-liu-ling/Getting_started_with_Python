import matplotlib.pyplot as plt
import numpy as np

#初始化数据
x_values = list(range(1, 101))
y_values = [x**2 for x in x_values]

#设置样式
plt.style.use('seaborn')

#绘制图
#plt.scatter(x_values, y_values, s=20, c=y_values, cmap=plt.cm.Greens,alpha=0.5)  #alpha是透明度参数
plt.scatter(x_values, y_values, s=10, c='red',alpha=0.5)  #alpha是透明度参数

#设置图表标题并给坐标轴加上标签
plt.title("square", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("square of value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个轴的取值范围
plt.xlim(0, 110)
plt.ylim(0, 11000)

#设置坐标轴的刻度
ax_0 = plt.gca()
ax_0.locator_params('x', nbins=11)
my_y_ticks = np.arange(0, 11001, 1000)
plt.yticks(my_y_ticks)


plt.show()