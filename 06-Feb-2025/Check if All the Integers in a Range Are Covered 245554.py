# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        ranges.sort()
        cover = left
        
        for start, end in ranges:
            if start > cover:
                continue
            if end >= cover:
                cover = end + 1
            if cover > right:
                return True
        
        return cover > right

        
        