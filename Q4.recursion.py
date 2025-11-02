a=int(input(":"))
def add(t):
    last_digit=t%10
    new_number=t//10
    if t==0:
        return 0
    else: 
        return last_digit + add(new_number)
print(add(a))