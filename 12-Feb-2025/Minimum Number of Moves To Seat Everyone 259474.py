# Problem: Minimum Number of Moves To Seat Everyone - https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        first,second=0,0
        count=0
       
        while first<len(seats) and second<len(students):

            count+= abs(seats[first]-students[second])
            first+=1
            second+=1
          
        return count

            
        