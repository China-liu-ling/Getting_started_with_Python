import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime

#防止中文乱码
font_zh = fm.FontProperties(fname='C:\Windows\Fonts\simhei.ttf')

filename = 'death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #从文件中获取日期、最高温度和最低温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        c_high = (high-32)/1.8  #将华氏温度转换为摄氏温度
        c_low = (low-32)/1.8  #将华氏温度转换为摄氏温度
        dates.append(current_date)
        highs.append(c_high)
        lows.append(c_low)

#根据最高温度绘制图形
#设置图形样式
plt.style.use('seaborn')

#绘制图形
fig = plt.figure()
plt.plot(dates, highs, c='r', alpha=0.5)
plt.plot(dates, lows, c='b', alpha=0.5)

#给图形区域着色
plt.fill_between(dates, highs, lows, facecolor='b', alpha=0.1)

#设置图形的格式
title = "2018年每日最高温度和最低温度\n 美国加利佛尼亚州死亡谷"
plt.title(title, fontproperties=font_zh, fontsize=20)
plt.xlabel('', fontsize=14)
plt.ylabel('温度 (c)', fontproperties=font_zh, fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()
plt.show()