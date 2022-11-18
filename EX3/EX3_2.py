def EX3_2(nums):
  length = len(nums) - 1
  multiplication = []
  if length > 0:
    for i in range(0 ,length):
      j = i + 1
      mul = nums[i] * nums[j]
      multiplication.append(mul)
      multiplication.sort()
    return multiplication[length - 1]
  else:
    return "Error"
