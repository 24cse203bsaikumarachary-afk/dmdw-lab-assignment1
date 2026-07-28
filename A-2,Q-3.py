
print("Using user logic:")
data=[10,12,15,18,20,20,22,25]
l=len(data)
if l%2==0:
    median=(data[l//2-1]+data[l//2])/2
else:
    median=data[l//2]
print("Median:",median)
print("Using inbuilt library:")
import numpy as np
data=[10,12,15,18,20,20,22,25]
print("Median:",np.median(data))
