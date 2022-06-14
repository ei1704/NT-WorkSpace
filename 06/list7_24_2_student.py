import math

arr = [4, -9, 16, -4, 20]
print(arr)

# 変数arrの各要素を絶対値にし、変数arr_absに代入してください。
arr_abs = [abs(i) for i in arr]
print(arr_abs)

# 変数arr_absの各要素のeのべき乗と平方根を出力してください。
print([math.exp(i) for i in arr_abs])
print([math.sqrt(i) for i in arr_abs])
