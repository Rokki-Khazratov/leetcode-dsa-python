nums = [2,3,1,2,4,3]
target = 7

def minSubArrayLen(target, nums) -> int:
    begin = 0
    window_sum = 0
    best_len = float('inf')
    for end in range(len(nums)):
        window_sum += nums[end]
        while window_sum >= target:
            window_size = end-begin+1
            print(best_len, window_size)
            best_len = min(best_len, window_size)
            window_sum -= nums[begin]
            begin += 1
    if  best_len == float('inf'):
        return 0
    return best_len




print(minSubArrayLen(target, nums))