# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans,res=[],[]
        n=len(nums)
        def backTrack():
            if len(ans)==n:
                res.append(ans[:])
                return
            for num in nums:
                if not num in ans:
                    ans.append(num)
                    backTrack()
                    ans.pop()
        backTrack()
        return res



        