# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())
dragons = []
for _ in range(n):
    xi, yi = map(int, input().split())
    dragons.append((xi, yi))
dragons.sort()
 
for xi, yi in dragons:
    if s > xi:
        s += yi 
    else:
        print("NO")
        break
else:
    
    print("YES")