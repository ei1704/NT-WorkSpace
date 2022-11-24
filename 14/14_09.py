import re

pat = r"^\d+,\"(.+?)\",.+,(\d{3}-\d{3}-\d{4}),"

with open("sample.csv",'r',encoding='utf-8') as f:
  for line in f:
    #gprint(line)
    m = re.match(pat, line)
    if m:
      print(f'{m.group(1)} {m.group(2)}')

