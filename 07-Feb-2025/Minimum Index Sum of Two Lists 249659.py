# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_list1=defaultdict(int)
        dict_list2=defaultdict(int)
       
        for i in range(len(list1)):
            dict_list1[list1[i]]+=i
        for j in range(len(list2)):
            dict_list2[list2[j]]+=j
        min_sum = float('inf')
        result = []
       
        for k, v in dict_list1.items():
            if k in dict_list2:
                v2 = dict_list2[k]
                current_sum = v+ v2
                
               
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [k]
               
                elif current_sum == min_sum:
                    result.append(k)
        
        return result
        
    

        