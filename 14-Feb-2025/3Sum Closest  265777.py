# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float('inf')
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum
                
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum  
        
        return closest


