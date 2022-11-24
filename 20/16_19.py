#\s\d{1,2}\.\s(.+):を一行ずつ見る
import re
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

path = 'agaricus-lepiota.names'
pat_skip = '^(\d)\.\s.+'
colums = ["classes"]

with open(path,'r') as f:
  read_flag = False

  for s in f:
    head_num = re.search(pat_skip,s)
    if(head_num and head_num.group(1) == '7'):
      read_flag = True
    elif(head_num and head_num.group(1) == '8'):
      read_flag = False

    if(read_flag):
      m = re.search('\s\d{1,2}\.\s(.+):', s)
      if(m and m.group(1)):
        #group(1)で正規表現の()内のみ抽出する
        #print(m.group(1))
        colums.append(m.group(1))

#header=None...一行目をヘッダーとして読み込まない
mush_data = pd.read_csv('agaricus-lepiota.data', header=None)

mush_data.columns = colums
#print(mush_data)

#print(mush_data[['gill-size', 'gill-attachment', 'odor', 'cap-color']])

#get_dumies...カテゴリ変数をダミー変数に変換する
mush_data_dummy = pd.get_dummies(mush_data[["gill-size","gill-attachment","odor","cap-color"]])

#値ごとのフラグに変化した
#print(mush_data_dummy)


#mush_data['classes']の全ての値にラムダ式を適用するためのmap
#classesの値がpなら1,eなら0になった
#lambdaは値がpだったら1,それ以外を0にするためのもの
mush_data_dummy['flg'] = mush_data['classes'].map(lambda x: 1 if x == 'p' else 0)
#print(mush_data_dummy)

#テーブルからflg列を削除する
X = mush_data_dummy.drop("flg", axis=1)
Y = mush_data_dummy["flg"]
train_X, test_X, train_y, test_y = train_test_split(X, Y, random_state=42)
model = DecisionTreeClassifier()
model.fit(train_X, train_y)
model.predict(test_X)
print('正解率は{}'.format(model.score(test_X, test_y)))