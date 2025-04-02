# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        def backtarck(path,open,close):
            if len(path)==2*n:
                ans.append("".join(path[:]))
                return
            if open<n:
                path.append("(")
                backtarck(path,open+1,close+1)
                path.pop()

            if close>0:
                path.append(")")
                backtarck(path,open,close-1)
                path.pop()
            return
        backtarck([],0,0)
        return ans
    
        