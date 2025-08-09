# backtracking problem is always brute force


nums = [1,2,3]
n = len(nums)

result = []


def backtrack(per) :
    if len(per) == n :
        result.append(per[:])
        return 
    
    for i in nums :
        if i in per :
            continue 
        
        #include
        per.append(i)
        backtrack(per)
        #exclude
        per.pop()

backtrack([])

for i in result :
    print(i)