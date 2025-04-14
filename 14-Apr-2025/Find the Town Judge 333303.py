# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        
        trust_count = [0] * (n + 1)
        
        for a, b in trust:
            trust_count[a] -= 1
            trust_count[b] += 1
        
        for person in range(1, n + 1):
            if trust_count[person] == n - 1:
                return person
        
        return -1
           
        