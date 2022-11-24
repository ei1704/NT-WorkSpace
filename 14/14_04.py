data = [(1, 5), (4, 2), ("abc", 3)]
fswap = lambda x,y:(y,x)
for s,t in data:
  print( fswap(s, t) )