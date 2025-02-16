# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, data):
        file_map = defaultdict(list)

        for entry in data:
            parts = entry.split()
            dir_path = parts[0]
            
            for file_info in parts[1:]:
                file_name, file_content = file_info.split('(')
                file_content = file_content[:-1]
                
                file_map[file_content].append(f"{dir_path}/{file_name}")
        
        result = []
        for files in file_map.values():
            if len(files) > 1:
                result.append(files)
        
        return result

        