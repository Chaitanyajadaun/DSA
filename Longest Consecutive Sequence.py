nums=sorted(set(nums))
if len(nums)==0:
    return 0
count=1
ans=1
for i in range(len(nums)-1):
    if nums[i]==nums[i+1]-1:
        count+=1
    else:
        count=1
    if count>ans:
        ans=count
return ans