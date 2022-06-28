#to know more about the Goldbach's conjecture try out their wikipedia page linked here https://en.wikipedia.org/wiki/Goldbach%27s_conjecture

#this function defines if a number is prime or not
def isPrime(num):
  if num == 2:
    return num
  else:
    for i in range(2,num):
      if num%i==0:
        break
      else:
        return num

#this function expresses the number as a sum of two primes
def goldbach(num):
    for i in range(num+1):
        num1 = i+1
        num2 = num-i-1
        if isPrime(num1) == num1 and isPrime(num2) == num2:
            print(f"{num1}+{num2}={num}")

#calling the function
goldbach(19)
