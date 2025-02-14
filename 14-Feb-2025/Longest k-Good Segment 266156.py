# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 1
l = 0
start = 0
end = 0
a_dict = defaultdict(int)
for r in range(n):
    a_dict[a[r]] += 1
    while len(a_dict) > k:
        a_dict[a[l]] -= 1
        if a_dict[a[l]] == 0:
            del a_dict[a[l]]
        l += 1
    if (r - l + 1) > count:
        count=r-l+1
        start=l
        end=r
print(start+1,end+1)
