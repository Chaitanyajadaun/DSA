arr={}
for i in range(len(nums)):
    if nums[i]not in arr:
        arr[nums[i]]=1
    else:
        arr[nums[i]]+=1

for j in arr:
    if arr[j]>1:
        return True
return False