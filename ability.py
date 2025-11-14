def tavan(n, t):
    ''' 
    this function return tavan 
    '''
    javab = 1
    for i in range(t): # i mans walk on the numebr (t) 
        javab *= n  
        
    return javab


my_num=tavan(2, 2)
print(my_num)