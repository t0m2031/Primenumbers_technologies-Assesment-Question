def is_part_of_series(lst):
    '''Logic: suppose for n=10 the given function f(n) will yeild a series like:
    series = [0,1,3,7,15,31,63,127,255]
    To check if each element in input list lst is part of that series, we can add
    1 to the element in lst and check if it is a power of 2'''
    
    for ele in lst:
        var = ele+1
        # All power of two numbers have only one bit set. 
        # If we subtract a power of 2 numbers by 1 then 
        # all unset bits after the only set bit become set
        # and the set bit become unset.
        if not (var and (not(var & (var - 1))) ):
            return ("No")
    # Returns Yes if each element of input list is part of the series 
    # given by the function f(n)
    return ("Yes")   


size = int(input().strip())
lst=list(map(int,input().strip().split()))
op = is_part_of_series(lst)
print(op)