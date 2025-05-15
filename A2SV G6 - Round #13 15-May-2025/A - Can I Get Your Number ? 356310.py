# Problem: A - Can I Get Your Number ? - https://codeforces.com/gym/607625/problem/A

n = int(input())
a = sorted([input().strip() for _ in range(n)])
f_s, l_s = a[0], a[-1]
i = 0
while i < len(f_s) and f_s[i] == l_s[i]:
    i += 1
print(i)