import pandas as pd

df = pd.read_excel('fruits.xlsx')

print(df)
print()

print(df.iloc[:,[0,2,1]].transpose())
print()

print(df.T.loc[['fruits','year','time'],:])

print(df.T.iloc[[0,2,1],:])
print()

