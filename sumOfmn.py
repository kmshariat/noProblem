#sumOfmn function returns the sum of multiples of two numbers m and n between a certain limit

def sumOfmn(num1, num2, limit):
    count_num1 = limit//num1
    count_num2 = limit//num2
    count_num1_num2 = limit//(num1*num2)
    
    sum_num1 = (count_num1*(2*num1+(count_num1-1)*num1))/2
    sum_num2 = (count_num2*(2*num2+(count_num2-1)*num2))/2
    sum_num1_num2 = (count_num1_num2*(2*num1*num2+(count_num1_num2-1)*num1*num2))/2
    sum_num1_num2 = sum_num1+sum_num2-sum_num1_num2
    return sum_num1_num2
