"""
    In computer science and mathematics, the Josephus problem (or Josephus permutation) 
    is a theoretical problem related to a certain counting-out game.
    https://en.wikipedia.org/wiki/Josephus_problem
"""

def josephus(n : int, k : int) -> int:
    """
    Given n and k, this function returns the safe starting place.

    Args:
        n (int): Number of people in the circle.
        k (int): Steps to skip.
    Returns:
        int: Safe starting place.
    """    
    return n if n == 1 else (josephus(n - 1, k) + k-1) % n + 1

if __name__ == '__main__':

    print("The sade place is ", josephus(47, 5))