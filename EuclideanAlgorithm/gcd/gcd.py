def get_gcd(a, b):
    if(a == 0) :
        return b, 0, 1
    
    #this is a recursive algorithm
    #here is an article on recursion
    #https://www.cs.utah.edu/~germain/PPS/Topics/recursion.html
    #We need to be carful with recursion in python because of the way python 
    #executes recursive code. if we go too many layers deep with recursion in python 
    #we will get a stack overflow error.
    #Here is an article on this - https://www.geeksforgeeks.org/python-handling-recursion-limit/
    gcd, x1, y1 = get_gcd(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y