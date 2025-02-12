# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k %= n
        arr1=[]
        arr2=[]
        for i in range(0,n-k):
            arr1.append(nums[i])
      
        for j in range(n-k,n):
            arr2.append(nums[j])
        
        arr2.extend(arr1)
        
        for i in range(len(nums)):
            nums[i] = arr2[i]
        