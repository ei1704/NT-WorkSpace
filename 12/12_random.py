a = 123
b = 45
m = 100007
x = 0
LOOP = 60000

result = dict.fromkeys(range(1,7),0)

for _ in range(LOOP):
  x = (a*x + b) % m
  rand = x/(m-1)
  dice = int(rand * 6) + 1
  result[dice] += 1

print(result)