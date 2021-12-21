import numpy as np
from scipy import linalg
from scipy.optimize import curve_fit as fit
import timeit
import random
import matplotlib.pyplot as plt
import time


def solve_n_time(n,a=-128,b=128,times=1):
    x=np.random.randint(a,b+1,n)
    A=np.random.randint(a,b+1,(n,n))
    b=[sum(x[i]*a[i] for i in range(n)) for a in A]
    
    return timeit.timeit("linalg.solve(A,b)","from scipy import linalg",number=times,globals=locals())




plt.plot(range(15), [np.log2(i) for i in times])
plt.yscale=('log')
plt.show()


def curve(x,a,b,n):
    return a*x**n+b

def n(m):

    times=np.zeros(m)
    for i in range(m):
        times[i]=solve_n_time(2**i,times=1)
        
    return fit(curve,[2**i for i in range(m)], times)[0][2] # = 2.77 za pierwszym, 2.24 za drugim
