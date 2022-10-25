def EX1_6(num):
  '''
  (int) -> int
  convert num to roman numbers
  >>> EX1_6(5)
  V
  '''
  romanversion = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
  if type(num) == int:
    if num > 0 and num <= 10:
      num = num - 1
      roman = romanversion[num]
      return roman
    else:
      answer = "Error"
      return answer
  else:
    answer = "Error"
    return answer
