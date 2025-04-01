# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(nums):
            if len(nums)<=1:
                return nums
            
            left_half=nums[:len(nums)//2]
            right_half=nums[len(nums)//2:]
            left=mergesort(left_half)
            right=mergesort(right_half)
            merged=merge(left,right)
            return merged
        def merge(left_half,right_half):
            arr=[]
            l=0
            r=0
            while l <len(left_half) and r<len(right_half):
                if left_half[l]<=right_half[r]:
                    arr.append(left_half[l])
                    l+=1
                else:
                    arr.append(right_half[r])
                    r+=1
            while  l <len(left_half):
                arr.append(left_half[l])
                l+=1
            while r<len(right_half):
                arr.append(right_half[r])
                r+=1
            return arr
        return mergesort(nums)
            

                   


     