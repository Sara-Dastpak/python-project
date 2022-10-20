def EX1_5(age):
  if age > 0 and age <= 1:
    answer = "Infant"
    return answer
  elif age > 1 and age < 13:
    answer = "Child"
    return answer
  elif age >= 13 and age < 20:
    answer = "Teenager"
    return answer
  elif age >= 20:
    answer = "Adult"
    return answer
  else:
    answer = "the age must be bigger than zero"
    return answer
