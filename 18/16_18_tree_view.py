from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions
import numpy as np
import matplotlib.pyplot as plt
import graphviz

X,y = make_classification(n_samples=100, n_features=2, n_redundant=0, random_state=42)

train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=42)

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

model = tree.DecisionTreeClassifier()
model.fit(train_X,train_y)
print(model.score(test_X,test_y))

print(tree.plot_tree(model))
# ここから追加
dot_data = tree.export_graphviz(model, out_file=None)
graph = graphviz.Source(dot_data)
# format指定をしないとpdf
graph.render("tree", format='png')

#C:\Users\s202049.TSITCL\Anaconda3\pkgs\graphviz-2.38-hfd603c8_2\Library\bin
#C:\Users\s202049.TSITCL\Anaconda3\Library\bin\graphviz