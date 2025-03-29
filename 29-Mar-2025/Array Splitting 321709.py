# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(a[-1] - a[0])
else:
    gaps = []
    for i in range(1, n):
        gaps.append(a[i] - a[i-1])
    gaps.sort(reverse=True)
    total_cost = a[-1] - a[0]
    total_cost -= sum(gaps[:k-1])
    print(total_cost)
