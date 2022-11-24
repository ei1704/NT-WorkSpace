from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions
import numpy as np
import matplotlib.pyplot as plt

X,y=make_classification(n_samples=100,n_features=2,n_redundant=0,random_state=42)

train_X,test_X,train_y,test_y = train_test_split(X,y,random_state=42)

from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()

model.fit(train_X,train_y)

print(model.score(test_X,test_y))

plt.xlim(-4.5,4.5)
plt.ylim(min(X[:, 1]) - 0.5, max(X[:, 1]) + 0.5)

plt.grid(True)
plt.title("classification data using DecisionTreeClassifier")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

output_X = np.concatenate([train_X, test_X])	# 出力用の全データ 学習用＋評価用 の順
output_y = np.concatenate([train_y, test_y])	# 出力用の全データ 学習用＋評価用 の順
scatter_kwargs = {'s': 100, 'edgecolor': None, 'alpha': 0.7}	# 散布図用表示設定
scatter_highlight_kwargs = {'s': 100, 'label': 'Test data', 'alpha': 0.7}	# 評価用表示設定
plot_decision_regions(output_X, output_y, model,
                      legend=1,
                      X_highlight=test_X,
                      scatter_kwargs=scatter_kwargs,
                      scatter_highlight_kwargs=scatter_highlight_kwargs)

plt.show()