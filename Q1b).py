s=str(input(":"))
def main(t):
    k=t.lower()
    empty=[]
    for i in "aeiou":
        empty.append(f"{i}:{k.count(i)}")
    return empty
print(main(s))