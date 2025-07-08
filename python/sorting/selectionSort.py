nums = [9,5,4,2]

length = len(nums)

for i in range(length - 1) :
    index = i 
    for j in range(i + 1, length) :
        if nums[index] > nums[j] :
            index = j
    nums[index], nums[i] = nums[i], nums[index]

print(nums)