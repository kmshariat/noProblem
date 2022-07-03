def kaprekar(num):
  pos1 = num//1000
  num = num%1000
  pos2 = num//100
  num = num%100
  pos3 = num//10
  num = num%10
  pos4 = num 
  positions = (pos1, pos2, pos3, pos4)
  beta = sorted(positions)
  alpha = beta[::-1]
  #alpha-beta will be the new number but I am out of ideas about handling the data types here. 
