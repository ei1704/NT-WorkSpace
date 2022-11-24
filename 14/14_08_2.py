import numpy as np

data = np.random.randint(0, 100, 100)


#print(list(filter(lambda x:x % 2,data)))
print(list(filter(lambda x:x % 2 == 1,data)))
