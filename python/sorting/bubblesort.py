#bubblesort
nums = [9,0,8,42]

for i in range(len(nums) - 1) :
    for j in range(len(nums) - i - 1) :
        if nums[j] > nums[j + 1] :
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)