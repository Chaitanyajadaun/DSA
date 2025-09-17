ans=[]
arr=[]

def findcomb(i,target,arr,ans):
    if (i==len(candidates)):
        if target == 0:
            ans.append(arr[:])
        return ans 
    if candidates[i]<=target:
        arr.append(candidates[i])
        findcomb(i,target-candidates[i],arr,ans)
        arr.pop()
    findcomb(i+1,target,arr,ans)
    
findcomb(0,target,arr,ans)
return ans