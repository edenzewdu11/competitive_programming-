# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths=path.split('/')
        for char in paths:
            if char=="." or char=="":
                continue
            elif char=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        return "/"+"/".join(stack)