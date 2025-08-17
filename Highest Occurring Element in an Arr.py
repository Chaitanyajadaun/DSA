def mostFrequentElement(self, nums):
        arr={}
        for i in nums:
            if i in arr:
                arr[i]+=1
            else:
                arr[i]=1
        maxx=0
        for j in arr:
            if arr[j]>maxx:
                maxx=j
        return maxx
            