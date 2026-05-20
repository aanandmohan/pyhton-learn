'''Word Counter in Complaint Message

A customer care system wants to count how many words are present in a complaint message.

Input:
Enter complaint: Delivery was delayed again today

Output:
Total words: 5'''

word=input("enter your complain ")
# print(len(word.split()))
count=1
for i in range(0,len(word)):
    if word[i]==" ":
        count+=1
print("total word is ",count)