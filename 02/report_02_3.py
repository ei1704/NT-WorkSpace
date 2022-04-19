import math

print(" x sin(x) cos(x) tan(x)")
for i in range(0,91,15):
  #sin(),cos(),tan()の引数はradiansなので変換
  r_i = math.radians(i)
  print(f"{i:02} {math.sin(r_i):0.4f} {math.cos(r_i):0.4f} {math.tan(r_i):0.4f}")