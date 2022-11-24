import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

# Ubuntu22.04上での実行時に以下のエラーが発生する
# libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: 共有オブジェクトファイルを開けません: そのようなファイルやディレクトリはありません (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
# libGL error: failed to load driver: iris
# libGL error: MESA-LOADER: failed to open iris: /usr/lib/dri/iris_dri.so: 共有オブジェクトファイルを開けません: そのようなファイルやディレクトリはありません (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
# libGL error: failed to load driver: iris
# libGL error: MESA-LOADER: failed to open swrast: /usr/lib/dri/swrast_dri.so: 共有オブジェクトファイルを開けません: そのようなファイルやディレクトリはありません (search paths /usr/lib/x86_64-linux-gnu/dri:\$${ORIGIN}/dri:/usr/lib/dri, suffix _dri)
# libGL error: failed to load driver: swrast
#
# 回避策：GPUの設定を変更
# https://bugs.launchpad.net/ubuntu/+source/matlab-support/+bug/1872277
# export MESA_LOADER_DRIVER_OVERRIDE=i965


# P.514 二項分類用データ生成
X, y = make_classification(
    n_samples=100, n_features=2, n_redundant=0, random_state=42)


# P.518 学習用と評価用にデータを分割
train_X, test_X, train_y, test_y = \
    train_test_split(X, y, random_state=42)
# train_test_split(X, y, test_size=0.25, random_state=42)

# P.520 ロジスティック回帰で学習
model = LogisticRegression()
model.fit(train_X, train_y)  # 学習用データでモデルを訓練・適合(fit)
model.predict(test_X)        # 評価用データに対するモデルの予測(predict)結果
print('正解率は{}'.format(model.score(test_X, test_y)))


# p.521 散布図を描く
# 学習用データは'.'印で，評価用データは'x'印でプロット
plt.scatter(train_X[:, 0], train_X[:, 1], c=train_y, marker='.',
            cmap=matplotlib.cm.get_cmap(name='bwr'), alpha=0.7)
plt.scatter(test_X[:, 0], test_X[:, 1], c=test_y, marker='x',
            cmap=matplotlib.cm.get_cmap(name='bwr'), alpha=0.7)


# 学習して導出した識別境界線をプロット
# 学習後のモデル内には二項を分類する境界直線の属性値が求まった
w0 = model.intercept_
w1 = model.coef_[0][0]
w2 = model.coef_[0][1]

# モデル内の属性値は境界直線の式を表す
#  w0 + (w1 * x) + (w2 * y) = 0
# 変形すると
#  y = -(w1 / w2) * x - (w0 / w2)
# つまり，
#  傾きが -(w1 / w2)
#  切片が -(w0 / w2)
Xi = np.linspace(-10, 10, 20)
Y = -(w1 / w2) * Xi - (w0 / w2)
plt.plot(Xi, Y)

# グラフのスケールを調整
plt.xlim(min(X[:, 0]) - 0.5, max(X[:, 0]) + 0.5)
plt.ylim(min(X[:, 1]) - 0.5, max(X[:, 1]) + 0.5)
# 別の書き方
# plt.axis([min(X[:, 0]) - 0.5, max(X[:, 0]) + 0.5,
#           min(X[:, 1]) - 0.5, max(X[:, 1]) + 0.5])

# タテヨコ比を 1 対 1 にする
plt.gca().set_aspect('equal', 'datalim')
# plt.axes().set_aspect('equal', 'datalim')
# *** この指定では、Warningが発生 ***
# MatplotlibDeprecationWarning:  Adding an axes using the same arguments
# as a previous axes currently reuses the earlier instance. In a future
# version, a new instance will always be created and returned.
#   Meanwhile, this warning can be suppressed, and the future behavior
# ensured, by passing a unique label to each axes instance.
#
# https://stackoverflow.com/questions/47953061/matplotlib-axes-collision-warning-when-setting-aspect-ratio
#

plt.grid(True)
plt.title("classification data using LogisticRegression")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()
