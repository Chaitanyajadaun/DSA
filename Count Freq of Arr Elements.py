def countFrequencies(nums):
        dic={}
        arr=[]
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        for i in dic:
            arr.append([i,dic[i]])
        return arr

nums = [1, 2, 3, 2, 1, 4, 5, 1]
print(countFrequencies(nums))