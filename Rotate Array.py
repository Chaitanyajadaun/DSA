#self approach (o(k*n))
for i in range(k):
    x=nums.pop()
    nums.insert(0,x)
return nums