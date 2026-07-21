def greatest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=c:
        return b
    else:
        return c
x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
print("greatest number:",greatest(x,y,z))
