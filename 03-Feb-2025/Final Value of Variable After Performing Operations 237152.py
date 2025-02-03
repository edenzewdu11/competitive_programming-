# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations



class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if operation == "++X" or operation == "X++":
                x += 1
            elif operation == "--X" or operation == "X--":
                x -= 1
        return x