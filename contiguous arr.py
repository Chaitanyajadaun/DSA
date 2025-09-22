#better method (0(n^2))
ans=0
for i in range(len(nums)):
    balance=0
    for j in range(i,len(nums)):
        if nums[j]==1:
            balance+=1
        else:
            balance-=1
        
        if balance==0:
            ans=max(ans,j-i+1)
return ans

#better method (0(n))

arr={0:-1}
summ=0
ans=0
for i in range(len(nums)):
    if nums[i]==1:
        summ+=1
    else:
        summ-=1

    if summ not in arr:
        arr[summ]=i
    else:
        x=i-arr[summ]
        ans=max(ans,x)
return ans