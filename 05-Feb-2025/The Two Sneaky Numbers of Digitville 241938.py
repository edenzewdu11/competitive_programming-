# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dictt=defaultdict(int)
        arr=[]
        for num in nums:
            dictt[num]+= 1
        for key,values in dictt.items():
            if values==2:
                arr.append(key)
        return arr


        