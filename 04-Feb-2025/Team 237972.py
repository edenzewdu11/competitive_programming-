# Problem: Team - https://codeforces.com/contest/231/problem/A

n = int(input().strip())
count = 0

for _ in range(n):
    problem = list(map(int, input().strip().split()))
    if sum(problem) >= 2:
        count += 1

print(count)