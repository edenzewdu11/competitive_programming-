# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

t = int(input())  
sizes = ["S", "M", "L"]  

for _ in range(t):
    a, b = input().split()  
    pos_a = sizes.index(a[-1])  
    pos_b = sizes.index(b[-1])  
    
    if a == b:
        print("=")
    
    elif pos_a < pos_b:
        print("<")
    elif pos_a > pos_b:
        print(">")
    else:
       
        if pos_a == 0: 
            if len(a) < len(b):
                print(">")
            else:
                print("<")
        else:  
            if len(a) < len(b):
                print("<")
            else:
                print(">")
