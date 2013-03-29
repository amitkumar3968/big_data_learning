import matplotlib.pyplot as plt
import numpy as np
import random

t = np.arange(0.0, 5.0, 0.2)
print t
#plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')

iter = range (0, 20)
range1 = [ x for x in iter if x%3!=0]
range2 = [ x for x in iter if x%2!=0]
range3 = [ x for x in iter if x%5!=0]

print range1
print range2
print range3


plt.plot(range1, 'r--',  range2, '-bs',  range3,  '-g^')
plt.xlabel('some numbers')
plt.show()
