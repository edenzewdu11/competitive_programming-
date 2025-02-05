# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

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
        

        