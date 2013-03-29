

def ackermann_func(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann_func(m-1,  1)
    elif m>0 and n>0:
        return ackermann_func(m-1, ackermann_func(m,  n -1) )
        
print ackermann_func(3, 4)
