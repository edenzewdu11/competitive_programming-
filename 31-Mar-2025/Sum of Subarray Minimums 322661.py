# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total_sum = 0
        n = len(arr)
        MOD = 10 ** 9 + 7
        
        next_smaller_idx = [n] * n
        prev_smaller_idx = [-1] * n
        
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                next_smaller_idx[stack.pop()] = i
            stack.append(i)
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                prev_smaller_idx[stack.pop()] = i
            stack.append(i)
        
        for i in range(n):
            left_count = (i - prev_smaller_idx[i])
            right_count = (next_smaller_idx[i] - i)
            total_sum = (total_sum + left_count * right_count * arr[i]) % MOD
        
        return total_sum



        