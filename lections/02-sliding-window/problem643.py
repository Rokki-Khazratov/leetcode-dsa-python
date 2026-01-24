nums = [1,12,-5,-6,50,3]


def findMaxAverage(nums, k: int) -> float:
    begin = 0
    window_sum = 0
    best_sum = 0
    for end in range(len(nums)) :
        window_sum += nums[end]
        window_size = end-begin+1
        if window_size == k:
            best_sum = max(best_sum, window_sum)
            window_sum -= nums[begin]
            begin += 1
    return best_sum / k





# Test input
nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))