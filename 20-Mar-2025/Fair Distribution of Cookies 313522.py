# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children=[0 for i in range(k)]
        fairness=float("inf")
        def  fairtrack(children,i):
            nonlocal fairness
            if i==len(cookies):
                fairness=min(fairness,max(children))
                return 
            


            for j in range(k):
                if children[j]+cookies[i]<=fairness:
                    children[j]+=cookies[i]
                    fairtrack(children,i+1)
                    children[j]-=cookies[i]
        fairtrack(children,0)
        return fairness

       
        