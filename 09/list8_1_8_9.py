import pandas as pd

# P.221 リスト8.1
fruits1 = {"orange": 2, "banana": 3}
print(pd.Series(fruits1))
print()

# P.227 リスト8.8
fruits2 = {"banana": 3, "orange": 4, "grape": 1, "peach": 5}
series2 = pd.Series(fruits2)
print(series2[0:2])
print()

# P.227 リスト8.9
print(series2[["orange", "peach"]])
