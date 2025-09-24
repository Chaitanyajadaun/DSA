arr=[]
for i in range(len(schedule)):
    x=schedule[i]
    if len(x)>2:
        for j in range(0,len(x),2):
            pair=schedule[i][j:j+2]
            arr.append(pair)
    else:
        arr.append(x)
        
arr.sort(key=lambda x: x[0])

merged=[arr[0]]
for i in range(1,len(arr)):
    if arr[i][0] <= merged[-1][1]:   
        merged[-1][1] = max(merged[-1][1], arr[i][1])
    else:
        merged.append(arr[i])

ans=[]
for i in range(len(merged)-1):
    if merged[i][1]<merged[i+1][0]:
        ans.append((merged[i][1],merged[i+1][0]))
print(ans)