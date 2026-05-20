word1=input("enter first word ")
word2=input("enter second word ")
if len(word1)!=len(word2):
    print("not matching word ")
else:
    for ch in word2:
        if word1.count(ch)!=word2.count(ch):
            print("not matching ")
    else:
        print("matching")
