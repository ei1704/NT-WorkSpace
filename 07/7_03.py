import numpy as np

a_score = np.array([70,80,50,60,70,75,70,85])
b_score = np.array([60,90,40,70,70,85,75,70])

print(f'A組の平均={np.average(a_score)}点')
print(f'B組の平均={np.average(b_score)}点')

print(f'A組の分散={np.var(a_score)}')
print(f'B組の分散={np.var(b_score)}')

print(f'A組の標準偏差={np.std(a_score)}')
print(f'B組の標準偏差={np.std(b_score)}')

print("\nA組のグラフ")
for i in a_score:
  for j in range(0,i,10):
    print("*",end="")
  if i%10 != 0:
    print("/")
  else:
    print()

print("\nB組のグラフ")
for i in b_score:
  for j in range(0,i,10):
    print("*",end="")
  if i%10 != 0:
    print("/")
  else:
    print()

#B組の方が分散と標準偏差が大きい
#つまりB組はA組に比べて成績にばらつきがあると言える