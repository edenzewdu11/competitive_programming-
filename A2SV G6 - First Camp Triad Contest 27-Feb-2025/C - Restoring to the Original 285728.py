# Problem: C - Restoring to the Original - https://codeforces.com/gym/589822/problem/C

x=int(input())
y=input()
zero=[]
one=[]
for i in range(x):
    if y[i]=="z":
        zero.append(0)
    elif y[i]=="n":
        one.append(1)   
one.extend(zero)
print(*one)