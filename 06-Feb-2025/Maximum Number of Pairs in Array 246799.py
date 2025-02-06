# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        dictt=defaultdict(int)
        count_pair=0
        count_not=0
        for i in nums:
            dictt[i]+=1
        for k,v in dictt.items():
            if v%2==0:
                count_pair+=v//2
            elif v>=3 and v%2!=0:
                count_pair+=(v-1)//2
                count_not+=1
            else:
                count_not+=1
        return [count_pair,count_not]


        