from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris = load_iris()

train_X,test_X,train_y,test_y = train_test_split(iris.data,iris.target,stratify=iris.target,random_state=42)

model = KNeighborsClassifier()
model.fit(train_X,train_y)
model.predict(test_X)
print('正解率は{}'.format(model.score(test_X,test_y)))