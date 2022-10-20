def EX1_3(side1, side2):
  if type(side1) == int and type(side2) == int:
    if side1 > 0 and side2 > 0:
      range = side1 + side2 - 1
      return range
    else:
      answer = "Such triangle dose not exist"
      return answer
  else:
    answer = "Such triangle dose not exist"
    return answer
