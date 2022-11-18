def EX3_6(listnum):
  listnum.sort()
  if len(listnum) == 0:
    return ":/"
  length = len(listnum) - 1
  interval = listnum[length] - listnum[0]
  for i in listnum:
    if i == interval:
      return ":)"
  else:
    return ":("
