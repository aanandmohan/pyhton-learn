exp=int(input('enter experince'))

s1=(30//100)*exp+exp
s2=(20//100)*exp+exp
s3=(10//100)*exp+exp

bonus= 30 if exp>10 else 20 if exp>5 else 10
print("Bonus  is  ",bonus,"%")