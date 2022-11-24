data = [(1, 5), (4, 2), (3, 3)]
fbigsmall = lambda x,y:(y,x) if y > x else (x,y)
for s,t in data:
  print( fbigsmall(s, t) )