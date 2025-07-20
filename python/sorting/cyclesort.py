a=[3,1,2,4,5]
i=0
while i < len(a):
    cur=a[i]-1
     # feels difficult, we can use i + 1        
    if a[i]!=a[cur]:
        a[i],a[cur]=a[cur],a[i]
    else: i+=1
print(a)

# with zero values in array
nums = [2,0,3,1]
i = 0 
while i < len(nums) - 1 :
    cur = nums[i] 
    
    if nums[i] != i :
        nums[i], nums[cur] = nums[cur], nums[i] 
    else :
        i += 1

print(nums)

nums = [3,1,2]

i = 0 
while i < len(nums) :
    #easy
    
    cur = nums[i] - 1

    if nums[i] == i + 1 :
        i += 1
    else :
        nums[i], nums[cur] = nums[cur], nums[i]

print(nums)