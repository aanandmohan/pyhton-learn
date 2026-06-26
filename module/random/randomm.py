import random

# print(random.uniform(10,25))
# print(random.randrange(1,10,2))
v=["virat","sita","kunal","lamanm","sitraman"]
print(random.choice(v))
print(random.choices(v,k=3))

number=random.randint(1,10)
print(number)
guess=int(input("enter a number "))
if guess== number:
    print("wow")
else:
    print("wromg betteer luck next time ")