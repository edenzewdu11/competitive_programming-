# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def first_position(l,r):
          
            while l<=r:
                mid=(l+r)//2
                if nums[mid]<target:
                    l=mid+1
                else:   
                    r=mid-1
            return l if l < len(nums) and nums[l] == target else -1
        def last_position(l,r):
            while l<=r:
                mid=(l+r)//2
                if nums[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return r if r >=0 and nums[r] == target else -1
        first,last=first_position(0,len(nums)-1),last_position(0,len(nums)-1)
        return [first,last]


        