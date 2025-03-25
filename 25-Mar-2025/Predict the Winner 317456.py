# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def backtrack(turn, nums):
            if len(nums) == 1:
                if turn == p1:
                    return nums[0], 0
                else:
                    return 0, nums[0]

            if turn == p1:
                selectFirst = backtrack(p2, nums[1:])
                selectLast = backtrack(p2, nums[:-1])
                if selectFirst[0] + nums[0] > selectLast[0] + nums[-1]:
                    return selectFirst[0] + nums[0], selectFirst[1]
                else:
                    return selectLast[0] + nums[-1], selectLast[1]
            else:
                selectFirst = backtrack(p1, nums[1:])
                selectLast = backtrack(p1, nums[:-1])
                if selectFirst[1] + nums[0] > selectLast[1] + nums[-1]:
                    return selectFirst[0], selectFirst[1] + nums[0]
                else:
                    return selectLast[0], selectLast[1] + nums[-1]

        p1, p2 = 1, 2
        score1, score2 = backtrack(p1, nums)
        return score1 >= score2




        