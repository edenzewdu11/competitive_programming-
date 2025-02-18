# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running = 0
        subarray_count = 0
        reminder_dictt = defaultdict(int)
        reminder_dictt[0] = 1
        
        for num in nums:
            running += num
            reminder=running%k
            if reminder in reminder_dictt:
                subarray_count +=reminder_dictt[reminder]
            reminder_dictt[reminder] += 1
        
        return subarray_count
        