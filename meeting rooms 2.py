start=[]
end=[]
for i in intervals:
    start.append(i[0])
    end.append(i[1])
start.sort()
end.sort()
p1=0
p2=0
rooms=0
maxrooms=0
while p1<len(start):
    if start[p1]<end[p2]:
        rooms+=1
        maxrooms=max(rooms,maxrooms)
        p1+=1
    else:
        rooms-=1
        p2+=1
return maxrooms