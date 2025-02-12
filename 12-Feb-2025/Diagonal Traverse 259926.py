# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        row, col = len(mat), len(mat[0])
        diagonals = {}

        for i in range(row):
            for j in range(col):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])

        result = []
        for k in range(row + col - 1):
            if k % 2 == 0:
                result.extend(reversed(diagonals[k]))
            else:
                result.extend(diagonals[k])

        return result

        