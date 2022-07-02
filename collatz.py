#this function simulates the collatz conjecture. more on this https://en.wikipedia.org/wiki/Collatz_conjecture
#this function takes one parameter as the initial number. if the number is even then it divides the number by 2 and assign the number to initial number. if the number is odd then it multiplies by 3 and adds 1 and assigns it to initial number.
#this conjecture states that the simulation stops when the number gets to 1

def collatz(initial_num):
  while initial_num != 1:
    if initial_num%2==0:
      initial_num = initial_num//2
      print(initial_num)
    else:
      initial_num = 3*initial_num +1 
      print(initial_num)
      
#collatz(7) will return a value of 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
