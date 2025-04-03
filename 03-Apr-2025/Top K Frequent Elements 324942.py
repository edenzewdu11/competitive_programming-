# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1
        
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]  
        for num, freq in frequency_map.items():
            buckets[freq].append(num)

        
        result = []
        for i in range(n, 0, -1):  
            if buckets[i]:
                result.extend(buckets[i])
            if len(result) >= k:
                break

        return result[:k]


        