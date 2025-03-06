# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

from collections import deque

class RecentCounter(object):
    def __init__(self):
        self.requests = deque()

    def ping(self, t):
        self.requests.append(t)
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)