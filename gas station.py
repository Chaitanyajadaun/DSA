start=0
fuel=0
if sum(gas) < sum(cost):   # Step 1: Feasibility check
    return -1
else:
    for i in range(len(gas)):
        fuel+=gas[i]-cost[i]
        
        if fuel<0:
            fuel=0
            start=i+1
    return start