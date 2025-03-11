# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations={"+","-","*","/"}
        for char in tokens:
            if char in operations:
                if stack:
                    b=stack.pop()
                    a=stack.pop()
                    if char=="+":
                        stack.append(a+b)
                    elif char=="-":
                        stack.append(a-b)
                    elif char=="*":
                        stack.append(a*b)
                    else:
                        stack.append(int(a/b))
            else:
                stack.append(int(char))
    
        return stack[0]

        
         