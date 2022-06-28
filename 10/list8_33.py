import pandas as pd

df = pd.read_excel('fruits.xlsx')

print(df)
print()

series = pd.Series({"fruits":"mango","year":2008,"time":7})
df = df.append(series, ignore_index=True)

df["test"] = [150,300,200,400,600,100]
df["test"] = 1

print(df)
