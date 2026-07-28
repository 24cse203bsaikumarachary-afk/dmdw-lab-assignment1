
print("Using user logic:")
data=[10,12,15,18,20,20,22,25]
fre={}
for i in data:
    if i in fre:
        fre[i]+=1
    else:
        fre[i]=1
mode=max(fre,key=fre.get)
print("Mode:",mode)
print("Using inbuilt library:")
import statistics as st
#data=[10,12,15,18,20,20,22,25]
print("Mode:",st.mode(data))
