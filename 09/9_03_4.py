import pandas as pd

list1 = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
list2 = [6, 7, 6, 5, 9, 6, 8]
series1 = pd.Series(list1, index=list2)

print(series1)
print(series1.index)
print(series1.values)
print(series1[6])
print(series1[6:])
