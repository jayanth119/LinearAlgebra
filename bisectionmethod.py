from math import  *
import time  
def evaluate(x):
    func = x-22/7
    return func

x,y=map(float,input().split())
print(evaluate(0))
i = 0
print("____________________________________________")
print("| a \t  b \t  f{a} \t  f{b} \t \t |")
print("|\t \t \t \t \t |")
print("____________________________________________")
c  = time.time()
ko = 0 
print(c)
while(evaluate(x)>0.0001 or evaluate(y)>0.0001):
    iter_start_time = time.time()
    q = evaluate(x)
    w = evaluate(y)
    print(f"| {x} \t  {y} \t {q}  \t {w}   \t |{i+1}")
    a = evaluate(x)
    b = evaluate(y)
    c = (x+y)/2
    v = evaluate(c)
    if(a<0 and v<0 and b>0 ) or (a>0 and v>0 and b<0 ):
        x = c 
    elif (a<0 and v>0 and b>0 ) or (a>0 and v<0 and  b<0):
        y=c
    iter_end_time = time.time()
    iter_time = iter_end_time - iter_start_time
    print(f"Iteration {ko+1} took {iter_time:.6f} seconds\n ")
    i+=1
    ko+=1 
d =  time.time()

print("____________________________________________")
print("the root of the polynomial is : ",x)
print("overal time ",c-d)
print("____________________________________________")
