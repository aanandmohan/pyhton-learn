s1="pprq"
s2="pqpq"
if len(s1)==len(s2):
    for ch in s1:
        if s1.count(ch)!=s2.count(ch):
            print("not balance ")
            break
    else:
        print("baalnce ")
else:
    print("not balance ")