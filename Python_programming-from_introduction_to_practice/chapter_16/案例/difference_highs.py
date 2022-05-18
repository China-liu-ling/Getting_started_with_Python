import csv
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from datetime import datetime

#防止中文乱码
font_zh = fm.FontProperties(fname='C:\Windows\Fonts\simhei.ttf')

filename_sitka = 'sitka_weather_2018_simple.csv'
with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #从文件中获取日期、最高温度
    dates, highs_sitka = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        c_high = (high-32)/1.8  #将华氏温度转换为摄氏温度
        highs_sitka.append(c_high)

filename_deathvalley = 'death_valley_2018_simple.csv'
with open(filename_deathvalley) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #从文件中获取日期、最高温度
    highs_deathvalley = []
    for row in reader:
        try:
            high = int(row[4])
        except ValueError:
            pass
        else:
            c_high = (high-32)/1.8  #将华氏温度转换为摄氏温度
            highs_deathvalley.append(c_high)

#根据最高温度绘制图形
#设置图形样式
plt.style.use('seaborn')

#绘制图形
fig = plt.figure()
plt.plot(dates, highs_sitka, c='r', alpha=0.5)
plt.plot(dates, highs_deathvalley, c='b', alpha=0.5)

#给图形区域着色
plt.fill_between(dates, highs_deathvalley, highs_sitka, facecolor='b', alpha=0.1)

#设置图形的格式
plt.title('2018年每日两地最高温的差', fontproperties=font_zh, fontsize=24)
plt.xlabel('', fontsize=14)
plt.ylabel('温度 (c)', fontproperties=font_zh, fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()

plt.show()