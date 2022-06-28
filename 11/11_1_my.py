import pandas as pd

df_sell = pd.read_csv('sell.csv')
df_user = pd.read_csv('user.csv')
df_item = pd.read_csv('item.csv')

df = pd.merge(df_sell,df_user,left_on="user",right_on="user_id",how="inner")
df = pd.merge(df,df_item,left_on="item",right_on="item_id",how="inner")

print(df)