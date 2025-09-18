intervals.sort(key=lambda x: x[0])
    print(intervals)
    arr=[intervals[0]]
    for i in range(len(intervals)):
        if intervals[i][0]<=arr[-1][1]:
            arr[-1][1]=max(arr[-1][1],intervals[i][1])
        else:
            arr.append(intervals[i])
    return arr