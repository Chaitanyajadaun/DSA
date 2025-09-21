#self approach (o(nlogn))
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

#best approach (o(n))

nums=set(nums)
maxx=0
for i in nums:
    if i-1 not in nums:
        count=1
        while i+1 in nums:
            count+=1
            i+=1
        maxx=max(count,maxx)
return maxx