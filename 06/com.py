import numpy as np

L = [0,1,2,3]

N = np.array(L)

print(L,type(L))
print(N,type(N),end="\n\n")

L = N.tolist()

print(N,type(N))
print(L,type(L))