# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill) - 1
        team_sum = skill[left] + skill[right]
        total_chemistry = 0
        
        while left < right:
            if skill[left] + skill[right] != team_sum:
                return -1
            total_chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return total_chemistry


        