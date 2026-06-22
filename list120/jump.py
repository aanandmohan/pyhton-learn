a=[2,3,1,1,4]
i=1
while i<=len(a):
    if a[i]==len(a)-i:
        print("True")
        
        break
    else:
        i+=a[i]
    
