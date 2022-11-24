def my_split(sentence, deleimiter=' '):
  strs = []
  strBuf = ""
  for chr in sentence:
    if chr == deleimiter:
      strs.append(strBuf)
      strBuf = ""
    else:
      strBuf += chr
      
  strs.append(strBuf)
  return strs

if __name__ == '__main__':
  test_sentence = "this is a test sentence."
  print(my_split(test_sentence))