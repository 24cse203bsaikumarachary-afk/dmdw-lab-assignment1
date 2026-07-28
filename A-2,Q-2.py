
print("Using user logic:")
data=[10,12,15,18,20,20,22,25]
total=0;
for i in data:
    total+=i;
mean=total/len(data)
print("Mean:",mean)
print("Using inbuilt library:")
import numpy as np
data=[10,12,15,18,20,20,22,25]
print("Mean:",np.mean(data))
