# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dictt=defaultdict(int)
        for i in nums:
            dictt[i]+=1
        arr=[]
        for key,values in dictt.items():
            if values==2:
                arr.append(key)
        return arr
        