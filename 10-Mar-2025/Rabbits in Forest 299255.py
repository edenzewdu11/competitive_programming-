# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
    
        res=0
        for num in count: 
            x=num+1
            while count[num]>0:
                res+=x
                count[num]-=x
        return res
        