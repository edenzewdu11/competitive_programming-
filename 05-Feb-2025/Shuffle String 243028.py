# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x=[0]*len(s)
        for i in range (len(s)):
            x[indices[i]]=s[i]
        
        return "".join(x)