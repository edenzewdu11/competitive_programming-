# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        new_list=[]
        for i in nums:
            index=abs(i)-1
            if nums[index]<0:
                new_list.append (abs(i))
            else:
                nums[index]=-nums[index]
  
        return new_list