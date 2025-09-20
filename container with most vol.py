maxx=0
i=0
j=len(height)-1
while i<j:
    area=min(height[i],height[j])*(j-i)
    maxx=max(area,maxx)
    if height[i]<height[j]:
        i+=1
    elif height[i]>height[j]:
        j-=1
    else:
        j-=1
return maxx