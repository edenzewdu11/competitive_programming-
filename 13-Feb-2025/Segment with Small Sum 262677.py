# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

x,y=map(int,input().split())
z=list(map(int,input().split()))
left=0
cur_sum=0
max_len=0
for right in range(x):
    cur_sum+=z[right]
    while cur_sum>y:
        cur_sum-=z[left]
        left+=1
    max_len=max(max_len,right-left+1)
print(max_len)