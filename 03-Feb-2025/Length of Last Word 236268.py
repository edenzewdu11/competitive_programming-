# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()
        if not words:
            return 0
        return len(words[-1])





        