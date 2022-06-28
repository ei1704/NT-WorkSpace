import pandas as pd

df = pd.read_excel('fruits.xlsx')

series = pd.Series({"fruits":"mango","year":2008,"time":7})
df = df.append(series, ignore_index=True)

print(df)
print()


df = df.drop(1,axis=0)

print(df)
