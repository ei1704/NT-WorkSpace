import math

def avg(targetArray):
  '''与えられた配列の平均を求める'''
  return sum(targetArray)/len(targetArray)

def dist(targetArray):
  '''与えられた配列の分散を求める'''
  arrayAvg = avg(targetArray)
  val = 0
  for i in targetArray:
    val += ((i - arrayAvg) ** 2)
  val /= len(targetArray)
  return val

def printGraph(targetArray):
  '''与えられた配列のグラフを出力する'''
  for i in range(100,0,-10):
    for j in targetArray:
      if j >= i:
        if 10 > j - i > 0:
          print("-",end="")
        else:
          print("*",end="")
      else:
        print(".",end="")
    print()

def main():
  a_score = [70,80,50,60,70,75,70,85]
  b_score = [60,90,40,70,70,85,75,70]

  print(f'A組の平均={avg(a_score)}点')
  print(f'A組の分散={dist(a_score)}')
  print(f'A組の標準偏差={math.sqrt(dist(a_score))}')
  #平方根は「** 0.5」でも求めることができる


  print()

  print(f'B組の平均={avg(b_score)}点')
  print(f'B組の分散={dist(b_score)}')
  print(f'B組の標準偏差={dist(b_score) ** 0.5}')

  print()
  print("A組のグラフ")
  printGraph(a_score)

  print()
  print("B組のグラフ")
  printGraph(b_score)

  #B組の方が分散と標準偏差が大きい
  #つまりB組はA組に比べて成績にばらつきがあると言える

if __name__ == "__main__":
  main()