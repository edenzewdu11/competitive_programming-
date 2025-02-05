# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x = defaultdict(list)
        for s in strs:
            sort_word = ''.join(sorted(s))
            x[sort_word].append(s)
        
        return list(x.values())

        