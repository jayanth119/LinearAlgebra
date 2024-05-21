from math import  *
import time 
def evaluate(x):
    func = x-22/7 
    return func 
x,y=map(float,input().split())
i = 0
print("____________________________________________")
print("| a \t  b \t  f{a} \t  f{b} \t \t |")
print("|\t \t \t \t \t |")
print("____________________________________________")
a = evaluate(x)
b = evaluate(y)
c = (x*evaluate(y)-y*evaluate(x))/(evaluate(y)-evaluate(x))
while(evaluate(x)>0.001 or evaluate(y)>0.001 or c>0.001):
    iter_start_time = time.time()
    print(f'({x},{y})')
    c = (x*evaluate(y)-y*evaluate(x))/(evaluate(y)-evaluate(x))
    v = evaluate(c)
    if(a<0 and v<0 and b>0 ) or (a>0 and v>0 and b<0 ):
        x = c
    elif (a<0 and v>0 and b>0 ) or (a>0 and v<0 and  b<0):
        y=c
    iter_end_time = time.time()
    iter_time = iter_end_time - iter_start_time
    print(f"Iteration {i+1} took {iter_time:.6f} seconds\n ")
    i+=1
print("____________________________________________")
print("the root of the polynomial is : ",x)
print("____________________________________________")
