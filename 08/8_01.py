IN_FILENAME = "sample.csv"
OUT_FILENAME = "output.csv"

with open(IN_FILENAME,"r",encoding='utf-8') as f:
  with open(OUT_FILENAME,"w",encoding='utf-8') as o:
    for line in f:
      o.write(line)