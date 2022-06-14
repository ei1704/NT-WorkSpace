from multiprocessing import Condition
import pandas as pd

#データのロード
dataframe = pd.read_csv('titanic.csv')

#データのサイズ
print(dataframe.shape)

#データのカラム
print(dataframe.columns)

#行列から必要な列を取り出す
print(dataframe['Age'])


#条件にマッチするデータを取りだす
print(dataframe.query('Age > 20'))
#それぞれの要素についてbooleanで返ってくる
#print(dataframe['Age'] > 20)

#行列から必要な行番号を指定して取り出す(0~2行目)
print(dataframe.loc[0:2])

#グループ分けと集計
print(dataframe.groupby(['Survived']).mean())
#reset_indexを実行することで返ってきた行列に対してインデックスが割り振られる
print(dataframe.groupby(['Survived']).mean().reset_index())

#新たな列を追加する
#ここではただ1を持つのみの列を追加
dataframe=dataframe.assign(
    One = 1
)
#print(dataframe.columns)
print(dataframe.loc[0])

#条件にあったセルだけを書き換える
#生存者はOneの値を0に設定する
dataframe.loc[dataframe['Survived'] == 1, ['One']] = 0
print(dataframe.loc[0:2])

#setやリストに存在する値のデータだけを取り出す
#Embarked が S または C のデータを取り出す
target_set = set(["S", "C"])
condition = dataframe['Embarked'].isin(target_set)
#booleanで返ってくる
print(dataframe[condition])