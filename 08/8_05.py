import pandas as pd

dataframe = pd.read_excel('titanic.xlsx')

print(dataframe.shape)#(行、列)
print(dataframe.shape[0])#行
print(dataframe.shape[1])#列
print(dataframe.columns)#列の名前が格納された配列
print(dataframe.index)#行数