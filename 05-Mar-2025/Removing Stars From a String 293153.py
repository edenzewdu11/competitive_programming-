# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution(object):
    def removeStars(self, s):
        stack = []

        for i in range(len(s)):
            if s[i] == "*" :
                stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)
