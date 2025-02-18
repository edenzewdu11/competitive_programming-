# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        running_sum=0
        sum_map=defaultdict(int)
        sum_map[0]=1
        count=0
        for num in nums:
            running_sum+=num
            if running_sum-goal in sum_map:
                count+=sum_map[running_sum-goal]
            sum_map[running_sum] += 1
        return count
        