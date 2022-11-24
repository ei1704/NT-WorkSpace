from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()

train_X,test_X,train_y,test_y = train_test_split(iris.data,iris.target,stratify=iris.target,random_state=42)

X = []
Y = []

for k in range(1,101,2):
  model = KNeighborsClassifier(n_neighbors=k)
  model.fit(train_X,train_y)
  model.predict(test_X)
  Y.append(model.score(test_X,test_y))
  X.append(k)

plt.ylim(0, 1)
plt.grid(True)
plt.plot(X,Y)
#plt.show()
plt.savefig('Fig1.png')
