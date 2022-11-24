data = ["abcdef","xyz","漢字文字","トライデント"]
fgt5 = lambda x: True if len(x) >= 5 else False
for s in data:
  print(f"{fgt5(s)} {s}")
