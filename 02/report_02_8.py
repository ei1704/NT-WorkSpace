list_99 = []
for i in range(1,10):
  list_temp=[]
  for j in range(1,10):
    list_temp.append(i*j)
  list_99.append(list_temp)

#print(list_99)

print("[",end="")
for i in list_99:
  if i[0] == 9:
    print(i,end="]\n")
  else:
    print(i,end=",\n")
  