# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        end=len(piles)-2
        i=0
        maxsum=0
        while i<len(piles)/3:
            maxsum+=piles[end]
            end-=2
            i+=1
        return maxsum

        