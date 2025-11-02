s=str(input(":"))
def fun(s):
    k=1
    t=s.lower()
    x="abcdefghijklmnopqrstuvwxyz"
    for i in x:
        if i in t:
            pass
        else:
            k=0
            break
    return k==1
print(fun(s))