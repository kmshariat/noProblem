#this function can return the largest value of a given tuple
def largest(*list):
    list = sorted(list)
    return list[-1]
#largest(0,9,28,6,-1,2) will return a value of 28

#this function can return the smallest value of a given tuple
def smallest(*list):
    list = sorted(list)
    return list[0]
  #largest(0,9,28,6,-1,2) will return a value of -1
