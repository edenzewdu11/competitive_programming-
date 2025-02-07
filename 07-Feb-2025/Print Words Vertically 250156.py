# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/



class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        arr = []

        for i in range(max_len):
            string = ""
            for word in words:
                if i < len(word):
                    string += word[i]
                else:
                    string += " "
            arr.append(string.rstrip())

        return arr



        