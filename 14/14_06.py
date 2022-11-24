def my_resplit(sentence, deleimiters=' '):
  strs = []
  strBuf = ""
  for chr in sentence:
    if chr in deleimiters:
      strs.append(strBuf)
      strBuf = ""
    else:
      strBuf += chr
  
  strs.append(strBuf)
  return strs

if __name__ == '__main__':
  test_sentence = "this,is a.test,sentence"
  print(my_resplit(test_sentence,', .'))