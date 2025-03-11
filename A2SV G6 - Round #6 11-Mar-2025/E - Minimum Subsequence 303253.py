# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t=int(input())
for _ in range(t):
    n=int(input())
    
    seq=input()
    stack0=[]
    stack1=[]
    answer=[]
    temp=0
    for i in range(n):
        if seq[i]=="0" and stack1:
            val = stack1.pop()
            stack0.append(val)
            answer.append(val)
        elif seq[i]=="1" and stack0:
            val = stack0.pop()
            stack1.append(val)
            answer.append(val)
        else:
            temp+=1
            if seq[i] == "0": stack0.append(temp)
            else: stack1.append(temp)
            answer.append(temp)
        # if seq[i]=="0":
        #     stack0.append(temp)
        # else:
        #     stack1.append(temp)
    print(temp)
    print(*answer)

