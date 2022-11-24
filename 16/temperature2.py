import matplotlib.pyplot as plt
import pandas as pd
import time

temp = pd.read_csv('raw_data.csv')


plt.figure(figsize=(16, 5))

temp['hour'] =  temp.time.str[:2]

temp_g = temp.groupby(['date','hour'],as_index=False).mean()

x = temp_g[temp_g.date == '2022-09-26']['hour']
temp_26 = temp_g[temp_g.date == '2022-09-26']['temperature']
temp_27 = temp_g[temp_g.date == '2022-09-27']['temperature']
temp_28 = temp_g[temp_g.date == '2022-09-28']['temperature']

plt.grid(True)
plt.title("Temperature in my living")
plt.xlabel("hour")
plt.ylabel("temperature")
plt.plot(x,temp_26,label="9/26")
plt.plot(x,temp_28,label="9/28")
plt.plot(x,temp_27,label="9/27")

#右上に線のラベルを出力
plt.legend()

plt.show()

"""
#temp_g = temp.groupby(['date','hour'],as_index=False).mean()

plt.plot(temp_g)

plt.show()
-----

#y = temp.temperature
y = temp[temp.date == "2022-09-26"]['temperature']
x = temp[temp.date == "2022-09-26"]['time']

plt.figure(figsize=(16, 5))

plt.plot(x,y)

plt.xticks(rotation='vertical')

plt.show()
"""