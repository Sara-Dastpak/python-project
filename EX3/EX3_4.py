def EX3_4(a, b, c):
  number = a
  for i in range(b):
    number = number + number
  if number % c == 0:
    return True
  else:
    return False
