# Problem: D - Life Across the Stars - https://codeforces.com/gym/591928/problem/D

from collections import defaultdict
n=int(input())
events=defaultdict(int)
for _ in range(n):
    b,d=map(int,input().split())
    events[b]+=1
    events[d]-=1
years=sorted(events.keys())
maxP=0
year=0
currentP=0
for y in years:
    currentP+=events[y]
    if currentP>maxP:
        maxP = currentP
        year =y
print(year,maxP)