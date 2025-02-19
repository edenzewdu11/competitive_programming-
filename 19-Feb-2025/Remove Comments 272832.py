# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        linebuf = ""
        inblock = False

        for line in source:
            idx = 0
            while idx < len(line):
                if idx < len(line) - 1 and line[idx] == '/' and line[idx + 1] == '/' and not inblock:
                    break
                elif idx < len(line) - 1 and line[idx] == '/' and line[idx + 1] == '*' and not inblock:
                    inblock = True
                    idx += 1
                elif idx < len(line) - 1 and line[idx] == '*' and line[idx + 1] == '/' and inblock:
                    inblock = False
                    idx += 1
                elif not inblock:
                    linebuf += line[idx]
                idx += 1

            if linebuf and not inblock:
                result.append(linebuf)
                linebuf = ""

        return result
        