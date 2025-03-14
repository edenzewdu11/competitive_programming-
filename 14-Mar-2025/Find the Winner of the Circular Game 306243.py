# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arry =[]
        for i in range(1, n+1):
            arry.append(i)
        i = 0
        while n > 1:
            i = (i+k-1) % n
            arry.pop(i)
            n -= 1
        return arry[0]
            

        