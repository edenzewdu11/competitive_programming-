# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

n = int(input())
t = input()

res = []
i = 0
for step in range(1, n + 1):
    if i < n:
        res.append(t[i])
        i += step

print("".join(res))

