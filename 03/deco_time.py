import time


def run_time(func):
    '''関数の名前tお実行時間を表示するデコレータ'''
    def funcname(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        print(f'実行関数:{func.__name__} 実行時間:{time.time() - start_time}')
        return result
    return funcname

# main
@run_time
def test(n):
    for i in range(n):
        time.sleep(i)

test(3)
test(5)