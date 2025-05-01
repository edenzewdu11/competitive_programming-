# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/


class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        climbs = []
        for i in range(len(h) - 1):
            d = h[i + 1] - h[i]
            if d > 0:
                heapq.heappush(climbs, d)
            if len(climbs) > l:
                b -= heapq.heappop(climbs)
                if b < 0:
                    return i
        return len(h) - 1

        