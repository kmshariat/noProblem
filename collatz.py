def collatz(initial_num):
  while initial_num != 1:
    if initial_num%2==0:
      initial_num = initial_num//2
      print(initial_num)
    else:
      initial_num = 3*initial_num +1 
      print(initial_num)
      
collatz(7)
