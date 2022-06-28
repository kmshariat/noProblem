#compute function returns the number of multiples of num1 and num2 between a certain limit
def compute(num1, num2, limit):
    count_num1 = limit//num1
    count_num2 = limit//num2
    count_num1_num2 = limit//(num1*num2)
    count = count_num1+count_num2-count_num1_num2
    return count
compute(2,5,10)
