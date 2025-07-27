nums = [1,2,3,4]

n = len(nums) 

for i in range(n) :
    for j in range(i, n) :
        print(nums[i : j + 1], end =" ")
    print()