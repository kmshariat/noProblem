"""
    This python code simulates the collatz conjecture. 
    more on this https://en.wikipedia.org/wiki/Collatz_conjecture
"""

def collatz_sequence(num : int) -> list[int]:
    """
    It takes one parameter as the initial number. if the number is even then it 
    divides the number by 2 and assign the number to initial number. 
    if the number is odd then it multiplies by 3 and adds 1 and assigns it to initial number.
    this conjecture states that the simulation stops when the number gets to 1. 
    This is also known as 3+1 conjecture.
    This returns the list of numbers reaching to 1.

    Args:
        num (int): Intitial Number
        
    Returns:
        list[int]: Numbers reaching to 1.
    """  
    
    list = [num]
    while num != 1:
        if num%2==0:
            num = num//2
            list.append(num)   
        else:
            num = 3*num +1 
            list.append(num)   
        
    return list


def collatz_sequence_recur(num : int) -> list[int]:
    """
    Same as fuction collatz_sequence() but done recursively.

    Args:
        num (int): _description_

    Returns:
        list[int]: _description_
    """    
    
    list = [num]
    if num == 1 :
        return list               
    elif num % 2 == 0 :
        list.extend(collatz_sequence_recur(num//2))     
    else:
        list.extend(collatz_sequence_recur(num*3+1))    
    return list



if __name__ == "__main__":
    print(collatz_sequence(7))
    print(collatz_sequence_recur(7))
    