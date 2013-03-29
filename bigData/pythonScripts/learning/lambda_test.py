def function(x):
    if x % 2 == 0:
        return x

iter = range(1,  10)
print filter(function,  iter)
value = lambda x : x**2 + 2*x - 5
for item in iter:
    print value(item)
    
item_info = [ x for x in iter if x%3!=0]
print item_info

