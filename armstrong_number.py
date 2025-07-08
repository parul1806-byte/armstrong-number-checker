#armstrong no , 153 = 1**3+5**3+3**3
def armstrong_number(n):
  original = n # n must assign within a variable so that last we can compare from the oroginal value of n
  sum = 0
  while n > 0:
      digit = n%10
      temp = digit**3
      sum = sum+temp
      n = n//10 # n become zero at the end of loop so its original value must be saved
  if original == sum:# sum must be equal to the original value
        print("its is armstrong number")
  else:
        print("it is not a armstrong number ")

armstrong_number(153)