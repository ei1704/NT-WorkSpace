import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X,y = make_classification(
    n_samples=1000,n_features=4,n_informative=3,n_redundant=0,random_state=42
)
train_X,test_X,train_y,test_y = train_test_split(X,y,random_state=42)

depth_list = [i for i in range(1,11)]
accuracy = []

for max_depth in depth_list:
  model = DecisionTreeClassifier(max_depth=max_depth,random_state=42)
  model.fit(train_X,train_y)
  print(f"正解率は:{model.score(test_X,test_y)}")
  accuracy.append(model.score(test_X,test_y))

plt.plot(depth_list,accuracy)
plt.xlabel("max_depth")
plt.ylabel("accuracy")
plt.title("accuracy by changing max_depth")
plt.show()
