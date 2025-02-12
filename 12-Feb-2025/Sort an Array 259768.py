# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        maximum = max(nums)
        minimum = abs(min(nums))
        count = [0] * (maximum + minimum + 1)

        for num in nums:
            count[num + minimum] += 1

        target = 0
        for index, value in enumerate(count):
            for _ in range(value):
                nums[target] = index - minimum
                target += 1

        return nums