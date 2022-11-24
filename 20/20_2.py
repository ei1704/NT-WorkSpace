from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()

a = np.array(iris['target'])
b = np.array(iris['target_names'])


u, counts = np.unique(a, return_counts=True)
for i in u:
  print(f'{b[i].ljust(12)}:{counts[i]}')