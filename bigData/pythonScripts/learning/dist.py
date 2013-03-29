import math

def distance(x1,  x2,  y1,  y2):
    diffx = x2 - x1
    diffy = y2 - y1
    diffx_sqr = diffx**2
    diffy_sqr = diffy**2
    diff_xy = diffx_sqr + diffy_sqr
    diff_result = math.sqrt(diff_xy)
    return diff_result 
    
#x = distance(1, 2, 3, 4)
#print x
    
def factorial(n):
    if isinstance(n,  int) != True:
        print 'factorial is only defined for integers.'
        return None
    if n < 0:
        print 'factorial is not defined for negative integers.'
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if isinstance(n,  int) != True:
        print 'fibonacci is only defined for integers.'
        return None
    if n < 0:
        print 'fibonacci is not defined for negative integers.'
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

y = fibonacci(10)
print y

