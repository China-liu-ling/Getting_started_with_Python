import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from die import Die

#防止中文乱码
font_zh = fm.FontProperties(fname='C:\Windows\Fonts\simhei.ttf')
 
#创建一个D6
die = Die()

#掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequences = []
for value in range(1, die.num_sides+1):
    frequence = results.count(value)
    frequences.append(frequence)

#对结果进行可视化
#设置样式
plt.style.use('classic')

#绘制图形
plt.bar(list(range(1, die.num_sides+1)), frequences, facecolor='#9999ff', 
        edgecolor='white')

#在柱状图上标记数字
for x, y in zip(list(range(1, die.num_sides+1)), frequences):
    plt.text(x, y+0.05, '%d'%y, ha='center', va='bottom')

#设置题目和坐标轴
plt.title('掷骰子', fontproperties=font_zh, fontsize=24)
plt.xlabel('点数', fontproperties=font_zh,fontsize=14)
plt.ylabel('frequence', fontsize=14)

#设置每个轴的取值范围
plt.ylim(0, 200)

#设置坐标轴的刻度
my_y_ticks = np.arange(0, 201, 20)
plt.yticks(my_y_ticks)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#显示图形
plt.show()

"""
x_values = list(range(1, die.num_sides+1))
data = [bar(x=x_values, y=frequences)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷一个D6 1000次的结果',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data, 'layout': my_layout}, filename='d6.html')
"""