def EX3_3(direction):
  j = 0
  i = 0
  for item in direction:
    if item == "n":
      j = j + 1
    elif item == "s":
      j = j - 1
    elif item == "e":
      i = i + 1
    elif item == "w":
      i = i - 1
  if i == 3 and j == 2:
    return True
  elif i == -4 and j == 3:
    return True
  else:
    return False
