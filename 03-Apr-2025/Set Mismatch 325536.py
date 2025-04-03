# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        set_nums=set(nums)
        ans=[]
        for i in range(1,len(nums)+1):
            if count[i]==2:
                ans.append(i)
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                ans.append(i)
           
        return ans

        

        