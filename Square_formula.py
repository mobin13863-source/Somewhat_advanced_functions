def sum_of_squares(a, b):
    '''
    This function takes two integers and calculates the sum of their squares.
    '''
    
    sum_of_squares = a ** 2 + b ** 2  # this a Formula
    return sum_of_squares # return the formule 
 

num = int(input("give me a number"))# give a number from user
num1 = int(input('give me secone numbner')) # give a Second number
 
print(sum_of_squares(num, num1)) # and use the function

