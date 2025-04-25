# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
      
        visited = set()
        queue = deque([0])  # Start with room 0

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                for key in rooms[current]:
                    if key not in visited:
                        queue.append(key)

        return len(visited) == len(rooms)
