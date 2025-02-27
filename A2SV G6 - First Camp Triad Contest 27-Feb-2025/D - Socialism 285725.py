# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=sorted(map(int,input().split()),reverse=True)
    summ=0
    for i in range(n):
        summ+=a[i]
        if summ<x *(i+1):
            print(i)
            break
    else:
        print(n)