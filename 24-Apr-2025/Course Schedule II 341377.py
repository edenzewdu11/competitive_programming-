# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
       
        adj = defaultdict(list)
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        res = []
        
        while q:
            node = q.popleft()
            res.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return res if len(res) == numCourses else []

        
        