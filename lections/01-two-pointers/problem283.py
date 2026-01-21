def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    p1 = 0
    p2 = 0
    for i in range(len(nums)):
        if nums[p2] != 0:
            nums[p1],nums[p2] = nums[p2],nums[p1]
            p1 += 1
        p2 += 1
    return nums

# Test input
nums = [0,1,0,3,12]
print(moveZeroes(nums))