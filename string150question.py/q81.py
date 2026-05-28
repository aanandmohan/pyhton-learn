s=input("enter string ")
has=0
for ch in s:
    has=has*31+ord(ch)

print(has)