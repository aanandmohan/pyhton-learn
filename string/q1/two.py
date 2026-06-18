n=int(input("enter  number of plyers "))
player=[]
for i in range(n):
    id=int(input("enter palyer id "))
    name=input("enter player name ")
    run=int(input('enter run scored '))
    p=(id,name,run)
    player.append(p)

print("all players ")
for i in player:
    print(i)

print("highest score ")
hig=player[0]
for i in player:
    if i[2]>hig[2]:
        hig=i
print(" the highest score is ",hig)

print("highest score ")
hig=player[0]
for i in player:
    if i[2]<hig[2]:
        hig=i
print(" the lowest score is ",hig)

print("total")
total=0
for i in player:
    total+=i[2]
print("total run is ",total)
avg=total/n
print("average is ",avg)
print("palyer who socred run more than 50 ")
for i in player:
    if i[2]>50:
        print(i)
