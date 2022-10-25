def EX1_2(base, height):
  '''
  (float, float) -> float
  Return the area of the triangle
  >>> EX1_2(4, 3)
  6
  '''
  if base > 0 and height > 0:
    area = (base * height)/2
    return area
  else:
    answer = "Such triangle dose not exist"
    return answer
