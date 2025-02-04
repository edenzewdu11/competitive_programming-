# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution(object):
    def isPalindrome(self, s):
        ss = []
        for i in s:
            if i.isalnum():
                ss.append(i.lower())
        i = 0
        j = len(ss) - 1
        while i < j:
            if ss[i] != ss[j]:
                return False
            i += 1
            j -= 1
        return True


