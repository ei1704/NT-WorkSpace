import pandas as pd

df = pd.read_excel('fruits.xlsx')

print(df)
print()

print(df.loc[[2,3],['year','fruits']])