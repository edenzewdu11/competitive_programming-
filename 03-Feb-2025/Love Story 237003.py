# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

x=int(input())

y="codeforces"
z=list(y)

for i in range(x):
    s=input()
    count=0
    j=0
    y="codeforces"
    z=list(y)
    for k in s:
        if z[j]!=k:
            count+=1
        j+=1  
        
    print(count)

