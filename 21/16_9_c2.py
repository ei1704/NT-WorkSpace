import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# データを生成します
X, y = make_classification(n_samples=100, n_features=2,
                           n_redundant=0, random_state=42)
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=42)

c = [10 ** i for i in range(-5,5)] 
Y=[]
Y2=[]

for i in c:
    # モデルを構築してください
    model = LogisticRegression(C=i,random_state=42)

    # train_Xとtrain_yを使ってモデルに学習させてください
    model.fit(train_X, train_y)

    # test_Xに対するモデルの分類予測結果を出してください
    pred_y = model.predict(test_X)

    #print('正解率は{}'.format(model.score(test_X, test_y)))
    Y.append(model.score(test_X,test_y))
    Y2.append(model.score(train_X,train_y))
 
# グラフのスケールを調整します
#plt.xlim(min(c[:, 0]) - 0.5, max(c[:, 0]) + 0.5)
#plt.ylim(min(Y[:, 1]) - 0.5, max(Y[:, 1]) + 0.5)
#plt.axes().set_aspect("equal", "datalim")

# グラフにタイトルを設定します
plt.title("accuracy by changing c")
plt.semilogx(c,Y,label='accuracy of test_data')
plt.semilogx(c,Y2,label='accuracy of train_data')
# x 軸、y 軸それぞれに名前を設定します
plt.xlabel("C")
plt.ylabel("accuracy")
plt.legend()
plt.grid()

plt.show()

#print(model.score())