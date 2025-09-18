arr={}
for i in nums:
    if i not in arr:
        arr[i]=1
    else:
        arr[i]+=1
for j in arr:
    if arr[j]>int(len(nums)/2):
        return j