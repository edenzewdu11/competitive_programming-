# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution(object):
    def frequencySort(self, s):
        dictt = defaultdict(int)
        
        for i in s:
            dictt[i] += 1
        
        sorted_chars = sorted(dictt.items(), key=lambda x: x[1], reverse=True)
        
        result = ""
        for k, v in sorted_chars:
            result += k * v
        
        return result

        



        