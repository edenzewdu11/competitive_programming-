# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

x=int(input())
for _ in range(x):
    n=int(input())
    a=list(map(int,input().split()))
    l=0
    count=0
    aNew=sorted(a)
    if a==aNew:
        print (0)
        continue
    while l<n:
        r=l+1
        if  r<n and a[l]>a[r]:
            count+=1
            l=r+1
            
        else:
            l+=1
    print(count)