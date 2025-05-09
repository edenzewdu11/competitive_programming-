# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s=[]
        stack_t=[]
        for i in range(len(s)):
            if  s[i]=="#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(s[i])
      
        for i in range(len(t)):
            if t[i]=="#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(t[i])
      
        if stack_s==stack_t:
            return True 
        return False