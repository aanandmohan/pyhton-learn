nums=[1,2,3]
ans=[[]]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        print(nums[i:j])
        ans.append(nums[i:j])   
print(ans)