def productExceptSelf(self, nums: List[int]) -> List[int]:
    prod=1
    arr=[]
    x=0
    if len(nums)==0:
        return nums
    for k in nums:
        if k == 0:
            x+=1
            
    for j in range(0,len(nums)):
        if nums[j]!=0:
            prod=prod*nums[j]

    if x==0:
        for i in nums:
            arr.append(int(prod/i))
        
    elif x==1:
        for a in nums:
            if a==0:
                arr.append(prod)
            else :
                arr.append(0)
    elif x>1:
        for b in nums:
            arr.append(0)
    return arr


#another approach

def productExceptSelf(self, nums: List[int]) -> List[int]:
    prod=1
    arr=[]
    x=0
    if len(nums)==0:
        return nums
    for k in nums:
        if k == 0:
            x+=1
            
    for j in range(0,len(nums)):
        if nums[j]!=0:
            prod=prod*nums[j]

    if x==0:
        prefix = {}
        suffix = {}
        
        
        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        
        suffix[len(nums)-1] = 1
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        
        
        for i in range(len(nums)):
            arr.append(prefix[i] * suffix[i])
        
    elif x==1:
        for a in nums:
            if a==0:
                arr.append(prod)
            else :
                arr.append(0)
    elif x>1:
        for b in nums:
            arr.append(0)
    return arr