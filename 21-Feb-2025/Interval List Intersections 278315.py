# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        i = j = 0
        answer = []
        while i < len(firstList) and j < len(secondList):
            start_a, end_a = firstList[i]
            start_b, end_b = secondList[j]

            if start_b > end_a:
                i += 1
            elif start_a > end_b:
                j += 1
            else:
                answer.append([max(start_a, start_b), min(end_a, end_b)])
            
                if end_a > end_b:
                    j += 1
                else:
                    i += 1
        return answer



