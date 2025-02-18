# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sum = 0
        subarray_count = 0
        sum_map = defaultdict(int)
        sum_map[0] = 1
        
        for num in nums:
            cumulative_sum += num
            if cumulative_sum - k in sum_map:
                subarray_count += sum_map[cumulative_sum - k]
            sum_map[cumulative_sum] += 1
        
        return subarray_count

            


        

        