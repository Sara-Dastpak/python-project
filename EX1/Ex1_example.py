def Ex1_example(num_minutes):
  if type(num_minutes) == int:
    seconds = num_minutes * 60
    return seconds
  else:
    answer = "your input must be integer"
    return answer
