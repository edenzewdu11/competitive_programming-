# Problem: Sum - https://codeforces.com/contest/1742/problem/A

x=int(input())
for i in range(x):
    s=list(map(int, input().split())) 
    s.sort() 
    if s[0]+s[1]==s[2]:
        print("YES")
    else:
        print("NO")
