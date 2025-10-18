ans=float('inf')
nums.sort()
for i in range(len(nums)):
    start=i+1
    end=len(nums)-1
    while start<end:
        diff=target-nums[i]-nums[start]-nums[end]
        if abs(diff)<abs(target-ans):
            ans=nums[i]+nums[start]+nums[end]
        if diff>0:
            start+=1
        else:
            end-=1
return ans