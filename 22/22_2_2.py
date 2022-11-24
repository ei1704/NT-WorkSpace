from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from dtreeviz.trees import dtreeviz
from sklearn.tree import DecisionTreeClassifier

from sklearn import tree

iris = load_iris()


train_X, test_X, train_y, test_y = \
train_test_split(iris['data'], iris['target'],stratify=iris['target'],
test_size=0.25, random_state=0)

depth_list = [i for i in range (1,11)]

for max_depth in depth_list:

  model = DecisionTreeClassifier(max_depth=max_depth)
  model.fit(train_X, train_y) # 学習用データでモデルを訓練・適合(fit)
  model.predict(test_X) # 評価用データに対するモデルの予測(predict)結果
  print('正解率は{}'.format(model.score(test_X, test_y)))

  #print(tree.plot_tree(model))
  viz = dtreeviz(model, train_X, train_y, target_name='IRIS',
              feature_names=iris['feature_names'],
              class_names=list(iris['target_names']))
              
  viz.save('dtreeviz_iris2_{}.svg'.format(max_depth))

