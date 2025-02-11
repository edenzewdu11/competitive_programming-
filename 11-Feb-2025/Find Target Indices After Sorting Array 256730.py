# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        arr=[]
        for i in range(len(nums)):
            if nums[i]==target:
                arr.append(i)
        return arr


        