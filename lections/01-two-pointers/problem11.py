# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# (blue section) the container can contain is 49.


# height = [1,8,6,2,5,4,8,3,7]
height = [5,0,5,4,0,0,0,0,4]
def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        curr_min = min(height[left], height[right])
        width = right - left
        curr_area = curr_min * width 
        if curr_area > max_area:
            max_area = curr_area
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return max_area






# Test input
height = [5,0,5,4,0,0,0,0,4]
print(maxArea(height))