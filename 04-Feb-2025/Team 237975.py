# Problem: Team - https://codeforces.com/contest/231/problem/A

x=int(input())
count=0
for i in range (x):
    a,b,c=list(map(int,input().split()))
    
    if a == b ==c ==1:
        count+=1
    elif a ==b == 1 or a == c== 1 or b == c== 1:
        count+=1
    else:
        count+=0
print(count)