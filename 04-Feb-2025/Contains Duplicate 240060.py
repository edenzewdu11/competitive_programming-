# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictt=defaultdict(int)
        for i in nums:
            dictt[i]+=1
        for keys,values in dictt.items():
            if values>=2:
                return True
        return False
        
        