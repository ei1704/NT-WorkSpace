import math

func_list = [math.sqrt, math.exp, math.sin]
data_list = [0, 0.5, 1.0, 2]
go_func = lambda x,y:[y(i) for i in x] 

for f in func_list:
    ans = go_func(data_list,f)
    print(ans)
