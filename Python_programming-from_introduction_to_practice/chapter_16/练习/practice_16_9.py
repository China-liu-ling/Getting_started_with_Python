import csv
import plotly.express as px
import pandas as pd

#打开文件并从文件中获取数据
file_name = 'world_fires_1_day.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #获取经度、纬度和火灾强度
    lons, lats, brightness = [], [], []
    for row in reader:
        lon = float(row[1])
        lat = float(row[0])
        brightnesss = float(row[2])
        lons.append(lon)
        lats.append(lat)
        brightness.append(brightnesss)

#处理数据
data = pd.DataFrame(
    data=zip(lons, lats, brightness), columns=['经度', '纬度', '火灾强度']
)
data.head()

#绘制图形
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y': '纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=1400,
    height=800,
    title='aa',
    size='火灾强度',
    size_max=20,
)

fig.write_html('global_fire_brightness.html')