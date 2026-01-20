from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        #   [2,7,11,15]     9
        while left < right:
            current_sum = nums[left] + nums[right] 
            if current_sum == target:
                return [left, right]
            if current_sum > target:
                right -= 1
                print(nums[left], nums[right])
            else:
                left += 1
                print(nums[left], nums[right])
        return []


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [2,7,11,15], target = 9
    nums2 = [2, 3, 4]
    target2 = 6
    result1 = solution.twoSum(nums2, target2)
    print(f"Test 1: nums={nums2}, target={target2}, result={result1}")
    print(f"Expected: [0, 1] (indices of 2 and 7)")
    print()