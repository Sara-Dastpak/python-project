def EX3_2(list):
  mul = []
  i = 0
  if len(list) > 1 :
    while i < len(list)-1:
      mul[i] = list[i] * list[i+1]
  else:
    return "Error"
  mul.sort()
  answer = len(list) - 2
  return mul[answer]
