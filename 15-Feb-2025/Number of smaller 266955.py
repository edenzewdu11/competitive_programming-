# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
result = []
for x in b:
    while i < n and a[i] < x:
        i += 1
    result.append(i)

print(*result)