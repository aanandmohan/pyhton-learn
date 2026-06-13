login=["deepika","ram","ram","sita"]
c={}
for user in login:
    c[user]=c.get(user,0)+1
print(c)