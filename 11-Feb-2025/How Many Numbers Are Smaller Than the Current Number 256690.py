# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        result = []
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[j] < nums[i]:
                    count += 1
            result.append(count)
        return result

            

      