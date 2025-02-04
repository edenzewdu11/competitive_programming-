# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        dictt=defaultdict(int)
        arr=[]
        for i in nums:
            dictt[i]+=1
        n=n//3
        for key,values in dictt.items():
            if values>n:
                arr.append(key)
        return arr
        

        