import numpy as np

print('case1')
print(np.full((2,3,4) , -1))

print('\ncase2')
print(np.ones((2,3,4)) * -1)

print('\ncase3')
print(np.zeros((2,3,4)) - 1)

print('\ncase4')
print(np.array([[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]],[[-1,-1,-1,-1],
      [-1,-1,-1,-1],[-1,-1,-1,-1]]]))

print('\ncase5')
array = [[[-1 for s in range(4)] for j in range(3)] for i in range(2)]
print(array)