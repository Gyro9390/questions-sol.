def hcf(a,b):
    k=min(a,b)
    l=[]
    for i in range (1,k+1):
        if a%i==0 and b%i==0:
            l.append(i)
        else:
            pass
    return max(l)

def lcm(x,y):
    return (x*y)//hcf(x,y)
first= int(input("Enter the first number:"))
second= int(input("Enter the second number:"))
print(f"the hcf of the 2 nubers is: {hcf(first,second)}")
print(f"the lcm of the 2 numbers is: {lcm(first,second)}")