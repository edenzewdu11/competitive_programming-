# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class UnionFind():
    def __init__(self,n):
        self.parent=[i for i in range(n+1)]
        self.size=[1]*(n+1)
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        px=self.find(x)
        py=self.find(y)
        if px==py:
            return True
        if self.size[x]<self.size[y]:
                self.parent[px]=py
                self.size[py]+=self.size[px]
        else:
                self.parent[py]=px
                self.size[px]+=self.size[py]
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        unionfind =UnionFind(n)
        for p,q in edges:
            if unionfind.union(p,q):
                return[p,q]

        