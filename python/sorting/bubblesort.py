nums = [9,0,8,6]

length = len(nums)

for i in range(length) :
    for j in range(length - i - 1) :
        if nums[j] > nums[j + 1] :
            nums[j],nums[j + 1] = nums[j + 1], nums[j]

print(nums)