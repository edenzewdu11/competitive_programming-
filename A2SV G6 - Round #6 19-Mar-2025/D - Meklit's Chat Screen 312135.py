# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque

n, k = map(int, input().split())
ids = list(map(int, input().split()))

scr = deque()
act = set()
for frnd in ids:
    if frnd in act:
        continue
    if len(scr) == k:
        rem = scr.pop()
        act.remove(rem)
    scr.appendleft(frnd)
    act.add(frnd)

print(len(scr))
print(*scr)
