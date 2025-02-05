# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        result = 0
        for word in words:
            word_count = Counter(word)
            count=0
            for i in range(len(word)):
                if word[i] in chars_count:
                    if word_count[word[i]]<=chars_count[word[i]]:
                        count+=1
            if count == len(word):
                result+=len(word)
                   
                        
        return result
