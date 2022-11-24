import numpy as np

data = np.random.randint(0, 100, 100)

odd = [x for x in data if x % 2 == 1]

print(odd)

