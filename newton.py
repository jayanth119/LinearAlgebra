from math import *
import time 
def der(x):
    c = 2*x
    return c
def func(x):
    d = x**2 - 4 
    return d
x =0.5
c  = time.time()
for i in range(20):
    iter_start_time = time.time()
    print("as",x)
    x = x-(func(x)/der(x))
    iter_end_time = time.time()
    iter_time = iter_end_time - iter_start_time
    print(f"Iteration {i+1} took {iter_time:.6f} seconds\n ")
d =  time.time()
