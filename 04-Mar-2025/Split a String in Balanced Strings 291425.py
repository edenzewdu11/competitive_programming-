# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dictt=defaultdict(int)
        count=0
        for i in range(len(s)):
            dictt[s[i]]+=1
            if dictt.get('L') == dictt.get('R'):
                count+=1
        return count
        


        