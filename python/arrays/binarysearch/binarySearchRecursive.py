def bs(start,end,tar):
    if start > end :
        print("Not found")
        return
    
    mid = start + (end - start) // 2
    
    if nums[mid] == tar:
        print("found",tar)
        return

    if nums[mid] < tar:
        bs(mid+1, end, tar)
    else:
        bs(start, mid - 1, tar)

nums = [0, 3, 5, 8, 9]
bs(0,len(nums)-1,7)
        