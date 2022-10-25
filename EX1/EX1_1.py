def EX1_1(number):
  '''
  (int) -> (int)
  >>> EX1_1(5)
  6
  '''
  if type(number) == int:
    answer = number + 1
    return answer
  else:
    answer = "your input must be integer"
    return answer
