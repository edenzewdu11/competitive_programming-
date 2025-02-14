# Problem: Books - https://codeforces.com/contest/279/problem/B

n,t=map(int,input().split())
a=list(map(int,input().split()))

summ=0
count=0
left=0
curr_summ=0
for i in range(n):
    curr_summ+=a[i]
    while curr_summ>t:
        curr_summ-=a[left]
        left+=1
    count=max(count,i-left+1)
print(count)