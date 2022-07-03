
def largest(*list):
    """ This function can return the max value of a given tuple
    Args:
        list (tuple)
    Returns:
        _type_: Max of Tuple
    """  
    return max(list)


def smallest(*list):
    """ This function can return the min value of a given tuple
    Args:
        list (tuple)
    Returns:
        _type_: Max of Tuple
    """    
    return min(list)


if __name__ == '__main__':
    print(largest(0,9,28,6,-1,2))
    print(smallest(0,9,28,6,-1,2))