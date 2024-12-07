def count_ways(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    #start first 2 steps
    prev1, prev2 = 1, 1

    # calculate steps upto n
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    
    return prev1

n = 5
print(f"The number of ways to climb {n} steps is: {count_ways(n)}")




