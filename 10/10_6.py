import pandas as pd

df = pd.read_excel('fruits.xlsx')

print(df.T.loc[["fruits","time","year"],range(0,5)])