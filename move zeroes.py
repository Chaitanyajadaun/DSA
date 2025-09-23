 x=0
for i in range(len(nums)):
    if nums[i]!=0:
        nums[x]=nums[i]
        x+=1
for j in range(x,len(nums)):
    nums[j]=0