# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dictt = defaultdict(int)
        
        for char in s:
            dictt[char] += 1
        
        values = list(dictt.values())
        
        return len(set(values)) == 1
