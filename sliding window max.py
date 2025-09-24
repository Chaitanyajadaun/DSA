#brute force approach O(n*k)
#self approach

arr=[]
for i in range(0,len(nums)-k+1):
    maxx=float("-inf")
    for j in range(i,i+k):
        if nums[j]>maxx:
            maxx=nums[j]
    arr.append(maxx)
return arr

#deque approach (o(n))

arr=[]
dq = deque()
for i in range(0,len(nums)):
    if len(dq)>0 and dq[0] == i-k:
        dq.popleft()
    while len(dq)>0 and nums[dq[-1]]<=nums[i]:
        dq.pop()
    dq.append(i)
    if i>=k-1:
        arr.append(nums[dq[0]])
return arr
        