# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        left_pointer, right_pointer = 0, len(height) - 1
        maximum_area = 0
        
        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            current_height = min(height[left_pointer], height[right_pointer])
            current_area = width * current_height
            maximum_area = max(maximum_area, current_area)
            
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return maximum_area
