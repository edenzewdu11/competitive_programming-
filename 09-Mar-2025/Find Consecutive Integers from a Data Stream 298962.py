# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.val=value
        self.k=k
        self.count=0
    def consec(self, num: int) -> bool:
        if num==self.val:
            self.count+=1
            return self.count>=self.k
        else:
            self.count=0
            return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)