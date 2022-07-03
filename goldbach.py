
"""
    To know more about the Goldbach's conjecture try out their
    wikipedia page linked here https://en.wikipedia.org/wiki/Goldbach%27s_conjecture

"""

import math

# This code makes sure sieve is called exactly once.
def run_once(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


primes = []
@run_once
def sieveSundaram() -> None:
	
	"""
		    In general Sieve of Sundaram, produces
			primes smaller than (2*x + 2) for a
			number given number x. Since we want
			primes smaller than MAX (10000), we reduce
			MAX to half. This array is used to
			separate numbers of the form i + j + 2*i*j
			from others where 1 <= i <= j
   
			This function is contributed by chandan_jnu, GFG.
			Modified By Abraar13.
	"""	
    
	marked = [False] * (int(10000 / 2) + 100)

	for i in range(1, int((math.sqrt(10000) - 1) / 2) + 1):
		for j in range((i * (i + 1)) << 1, int(10000 / 2) + 1, 2 * i + 1):
			marked[j] = True

	primes.append(2)

	for i in range(1, int(10000 / 2) + 1):
		if (marked[i] == False):
			primes.append(2 * i + 1)


def findPrimes(num : int) -> list[str]:

	sieveSundaram()
	
	i , ans = 0, []
 
	while (primes[i] <= num // 2):

		diff = num - primes[i]

		if diff in primes:
			ans.append(f"{primes[i]} + {diff} = {num}")
		i += 1
  
	ans.insert(0, f"There are {len(ans)} combinations : ")
 
	return ans



def print_goldbach(num : int) -> None:
    
    if (num <= 2 or num % 2 != 0):
        raise TypeError("Goldbach's conjecture it true for even num > 2")
        
    lst = findPrimes(num)
    for item in lst:
        print(item)


if __name__ == "__main__":

	print_goldbach(4)
	print_goldbach(20)
	print_goldbach(100)

