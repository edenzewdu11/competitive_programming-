# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        white, gray, black = 0, 1, 2
        color = [0] * len(graph)
        res = []

        def dfs(u):
            if color[u] == gray:
                return False
            color[u] = gray
            for v in graph[u]:
                if color[v] == black:
                    continue
                if not dfs(v):
                    return False
            color[u] = black
            res.append(u)
            return True

        for i in range(len(graph)):
            if color[i] == white:
                dfs(i)
        res.sort()
        return res
