import pandas as pd
index = ["apple","orange","banna","strawberry","kiwifruit"]
data = [10,5,8,12,3]
series = pd.Series(data,index=index)

#データ取り出し
print(series.values)

print("---")

#インデックス取り出し
print(series.index)

print("---")




#要素を追加
#追加する要素はSeriesの型に合わせる
#代入しないと追加が反映されない
series = series.append(pd.Series([5],index=["grape"]))
print(series)

print("---")

#要素を削除
#削除も追加同様に代入が必要
series = series.drop("strawberry")
print(series)

print("---")

#フィルタリング
conditions = [True,True,False,False,False]
print(series[conditions])

print("---")

#ソート
#インデックスのアルファベット順
print(series.sort_index())

#値の昇順
print(series.sort_values())

#降順、ascendingにFalseを指定する
print(series.sort_values(ascending=False))