#self approach (nlogn)

arr=[]
for i in nums:
    arr.append(i**2)
arr.sort()
return arr

#best approach (o(n))

i=0
j=len(nums)-1
arr=[]
while i<=j:
    if abs(nums[i])>abs(nums[j]):
        arr.append(nums[i]**2)
        i+=1
    else:
        arr.append(nums[j]**2)
        j-=1
arr.reverse()
return arr