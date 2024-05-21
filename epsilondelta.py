import matplotlib.pyplot as plt
import numpy as np
import math
e =float(input("enter epsilon"))
val = float(input("enter value "))
d=math.sqrt(e)
if (d<1 ):
    dl= 2
    inc = 0.1
else :
    dl = d
    inc =d/10    
L=[]
radius = int(dl**2)
x = np.linspace( -radius , radius , 150 )
y = np.linspace( -radius , radius , 150 )
a, b = np.meshgrid( x , y )
C = a ** 2 + b ** 2 - radius
figure, axes = plt.subplots() 
axes.contour( a , b , C , [0] )
axes.set_aspect( 1 )
plt.title( 'input of x and y values ' )
x = [0 for i in np.arange(-10,10,inc)]
y= [i for i in np.arange(-10,10,inc)]
x1= [ i for i in np.arange(-3,3,inc)]
y1=[i for i in np.arange(-3,3,inc)]
for i in np.arange(-dl,dl,0.1):
    for j in np.arange(-dl,dl,inc):
        di=(i**2)+(j**2)
        if(i==0 and j==0):
            continue
        else:
            if(di<d**2):
                a = 1
                z=(math.power(math.e,x)-(1+a)*x)/x
                L.append(z)
            else: 
                continue
        if(z>e):
            print("Limit doesnot exist",z)
            break
r= [0 for i  in range(len(L))]
xx,yy= np.meshgrid(r,L)
plt.axvline(x=val-e)
plt.axvline(x=val+e)
plt.plot(yy,xx)
plt.plot(x,y)
plt.plot(y,x)
plt.show()
print(L)
