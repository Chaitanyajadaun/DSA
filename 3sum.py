#first method (brute force)
arr=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in arr:
                            arr.append(triplet)
        return arr

#second method 
arr=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)-1):
                x=-(nums[i]+nums[j])
                if x in nums[j+1:]:
                    triplet = sorted([nums[i], nums[j], x])
                    if triplet not in arr:
                        arr.append(triplet)
        return arr

#third method (two pointer approach)
arr=[]
        a=len(nums)
        nums=sorted(nums)
        for i in range(a):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=a-1
            while(j<k):
                summ=nums[i]+nums[j]+nums[k]
                if summ<0:
                    j=j+1
                elif summ>0:
                    k=k-1
                else:
                    arr.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                    while (j<k and nums[j]==nums[j-1]):
                        j+=1
                    while (j<k and nums[k]==nums[k+1]):
                        k-=1
        return arr
