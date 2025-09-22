arr={0:1}
presum=0
count=0
for i in range(len(nums)):
    presum+=nums[i]
    if presum-k in arr:
        
        count+=arr[presum-k]
    if presum in arr:
        arr[presum]+=1
    else:
        arr[presum]=1
return count