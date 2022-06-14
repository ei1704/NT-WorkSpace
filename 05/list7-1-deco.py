import numpy as np
import time
from numpy.random import rand

def run_time(func):
    '''startとendを前後に出力するデコレータ'''
    def funcname(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'関数 {func.__name__}の実行時間{float(time.time()-start):.3f}[sec]')
        return result
    return funcname

N = 150
matA = np.array(rand(N,N))
matB = np.array(rand(N,N))
matC = np.array([[0.0] * N for _ in range(N)])

@run_time
def python_do():
    for i in range(N):
        for j in range(N):
            for k in range(N):
                matC[i][j] += matA[i][k] * matB[k][j]
    print(matC)

@run_time
def numpy_do():
    matC = np.dot(matA,matB)
    print(matC)

python_do()
numpy_do()