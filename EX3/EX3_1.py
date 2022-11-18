"""
سارا دست پاک
4012061016
"""
def EX3_1(n):
  i = 0
  while n != 1:
    if n % 2 == 0:
      n = n / 2
      i = i + 1
    elif n % 2 == 1:
      n = n*3 + 1
      i = i + 1
  return i
