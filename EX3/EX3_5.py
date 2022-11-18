def EX3_5(portions):
  distance = 0
  for i in portions:
    if i > 0:
      item = i
      distance = distance + item
    else:
      item = -1 * i
      distance = distance + item
  if distance == 25:
    return True
  else:
    return False
