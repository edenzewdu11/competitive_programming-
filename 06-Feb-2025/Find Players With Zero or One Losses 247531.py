# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dictt_win=defaultdict(int)
        dictt_loss=defaultdict(int)
        arr_win=[]
        arr_loss=[]
        for match in matches:
            dictt_win[match[0]]+=1
            dictt_loss[match[1]]+=1
        for k,v in dictt_win.items():
            if k not in dictt_loss:
                arr_win.append(k)
        for k,v in dictt_loss.items():   
            if v==1:
                arr_loss.append(k)
        arr_win.sort() 
        arr_loss.sort()   
        
        return [arr_win,arr_loss]


               