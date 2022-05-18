from random import randint
import matplotlib.font_manager as fm
import numpy as np
import matplotlib.pyplot as plt

#防止中文乱码
font_zh = fm.FontProperties(fname='C:\Windows\Fonts\simhei.ttf')

class Die:
    def __init__(self, num_sides=8):
        self.num_sides = num_sides
    
    def roll(self):
        return randint(1, self.num_sides)

#创建一个实例
die_0 = Die()
die_1 = Die()

#掷骰子并保存结果
results = []
for x in range(100):
    result = die_0.roll() + die_1.roll()
    results.append(result)

#分析结果
frequences = []
for value in range(1, die_0.num_sides+die_1.num_sides+1):
    frequence = results.count(value)
    frequences.append(frequence)

#对结果进行可视化
#设置样式
plt.style.use('classic')

#绘制图形
plt.bar(list(range(1, die_0.num_sides+die_1.num_sides+1)), frequences, facecolor='#9999ff', 
        edgecolor='white')

#在柱状图上标记数字
for x, y in zip(list(range(1, die_0.num_sides+die_1.num_sides+1)), frequences):
    plt.text(x, y+0.05, '%d'%y, ha='center', va='bottom')

#设置题目和坐标轴
plt.title('掷骰子', fontproperties=font_zh, fontsize=24)
plt.xlabel('点数', fontproperties=font_zh,fontsize=14)
plt.ylabel('频率', fontproperties=font_zh, fontsize=14)

#设置坐标轴的取值范围
plt.ylim(0, 30)
plt.xlim(1, 16)

#设置坐标轴的刻度
my_y_ticks = np.arange(0, 31, 5)
plt.yticks(my_y_ticks)
my_x_ticks = np.arange(2, 18, 1)
plt.xticks(my_x_ticks)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

#显示图形
plt.show()