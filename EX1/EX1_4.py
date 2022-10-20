def EX1_4(num):
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  if type(num) == int:
    if num > 0 and num < 8:
      num = num - 1
      day = days[num]
      return day
    else:
      answer = "Error"
      return answer
  else:
    answer = "Error"
    return answer  
