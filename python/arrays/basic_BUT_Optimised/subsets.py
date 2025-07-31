nums = [1,2,3]

result = []

#backtrack-neatly explained 

def backtrack(subset, i ) :
    if i == len(nums) :
        result.append(subset[:])
        return
    #include nums[i]
    subset.append(nums[i])
    backtrack(subset, i + 1)

    #exclude nums[i]
    subset.pop()
    backtrack(subset, i + 1)

backtrack([], 0)
print(result)

#backtracking with loops
result = []
def backtrackLoop(subset, start) :
    
    result.append(subset[:])

    for i in range(start, len(nums)) :
        subset.append(nums[i])

        backtrackLoop(subset, i + 1)

        subset.pop()

backtrackLoop([], 0)

print(result)