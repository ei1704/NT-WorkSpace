#\s\d{1,2}\.\s(.+):を一行ずつ見る
import re
path = 'agaricus-lepiota.names'
pat_skip = '^(\d)\.\s.+'
colums = []

with open(path,'r') as f:
  read_flag = False

  for s in f:
    head_num = re.search(pat_skip,s)
    if(head_num and head_num.group(1) == '7'):
      read_flag = True
    elif(head_num and head_num.group(1) == '8'):
      read_flag = False

    if(read_flag):
      m = re.search('\s\d{1,2}\.\s(.+):', s)
      if(m and m.group(1)):
        #group(1)で正規表現の()内のみ抽出する
        print(m.group(1))
        colums.append(m.group(1))

print(colums)