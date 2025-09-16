def position_placer(intervals,newInterval):
    if not intervals: 
        intervals = [newInterval]
    else:
        intervals.append(newInterval)  

    intervals.sort(key=lambda x: x[0]) 
    return intervals 
    
def finalizer(intervals):
    if not intervals:
        return []
    merged = [intervals[0]]   
    for i in range(1, len(intervals)):
        last = merged[-1]
        if intervals[i][0] <= last[1]:
                last[1] = max(last[1], intervals[i][1])  
        else:
            merged.append(intervals[i])   
    return merged
            
intervals=position_placer(intervals,newInterval)
return finalizer(intervals)     