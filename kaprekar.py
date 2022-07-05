"""
Kaprekar constant, or 6174, is a constant that arises when we take a 4-digit integer, 
form the largest and smallest numbers from its digits, and then subtract these two numbers. 
Continuing with this process of forming and subtracting, we will always arrive at the number 6174.
"""

import random


def kaprekar(num : int) -> None:
    if num == 6174: return
    num = int(''.join(sorted(str(num), reverse=True)))
    rev = int(''.join(sorted(str(num))))
    intermediate_num = num - rev
    print(f" {num} - {rev} = {intermediate_num}")
    kaprekar(intermediate_num)



if __name__ == '__main__':
  
  """
      Generates a random four digit number and applys the
      algorithm to make it reach 6174 and shows the steps.
  """  
  number = random.randint(1000,9999)
  kaprekar(number)