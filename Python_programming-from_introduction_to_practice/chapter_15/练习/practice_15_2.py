import matplotlib.pyplot as plt
import numpy as np

#初始化数据
x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

#绘制图形
plt.scatter(x_values, y_values, s=15, c=y_values, cmap=plt.cm.Blues)

#设置样式
plt.style.use('seaborn')

#设置标签
plt.title('cube', fontsize=24)
plt.xlabel('value', fontsize=14)
plt.ylabel('cube of value', fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个轴的取值范围
plt.xlim(0, 6)
plt.ylim(0, 130)

#设置坐标轴的刻度
my_x_ticks = np.arange(0, 7, 1)
plt.yticks(my_x_ticks)
my_y_ticks = np.arange(0, 131, 10)
plt.yticks(my_y_ticks)

plt.show()