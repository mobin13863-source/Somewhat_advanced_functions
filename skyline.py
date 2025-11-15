def  skyline(*args):
    '''
    thsi function Receive the heights of several buildings and
    return the tallest height.
    '''
    
    
    heights = 0  # I thought my maximum number is 0
    for i in args:
        if i > heights: # if my number(hrights of several) more than heights 
            heights = i # The height is equal to i, or the height of the buildings
        
    # we din't need else Because when the if condition is not met, it returns the value that we have set.     
    return heights 

print(skyline(3, 7, 15, 2, 9)) # in this line return 15 

print(skyline())# if print empty , return a zero(0)