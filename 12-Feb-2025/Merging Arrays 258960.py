# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n,m=map(int,input().split())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))
left,right=0,0
merged=[]
while left<n or right<m:
    if right==m or left<n and num1[left]<num2[right]:
        merged.append(num1[left])
        left+=1
    else:
        merged.append(num2[right])
        right+=1
print(*merged)
