# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

x = int(input())  

for _ in range(x):
    n = int(input())  
    r = list(map(int, input().split()))
    m = int(input())  
    b = list(map(int, input().split()))

    max_prefix_r, curr_r = 0, 0
    for num in r:
        curr_r += num
        max_prefix_r = max(max_prefix_r, curr_r)

    max_prefix_b, curr_b = 0, 0
    for num in b:
        curr_b += num
        max_prefix_b = max(max_prefix_b, curr_b)

    print(max_prefix_r + max_prefix_b)