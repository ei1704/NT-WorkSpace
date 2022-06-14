import random
import numpy as np
import time


def run_time(func):
    def funcname(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'関数 {func.__name__}の実行時間{float(time.time()-start):.3f}[sec]')
        return result
    return funcname

def print_countlist(counter):
    for i in range(1,7):
        print(f'{i}:{counter[i]}回')

    print('\n割合')

    for i in range(1,7):
        print(f'{i}:{counter[i]/10000*100}%')

@run_time
def dice():
    print("標準関数のサイコロ")
    count = [0 for i in range(7)]

    for i in range(10000):
        count[random.randint(1,6)] += 1

    print_countlist(count)

@run_time
def n_dice():
    print("\nnumpyのサイコロ")
    count = [0 for i in range(7)]

    for i in range(10000):
        count[np.random.randint(1,7)] += 1

    print_countlist(count)

dice()
n_dice()