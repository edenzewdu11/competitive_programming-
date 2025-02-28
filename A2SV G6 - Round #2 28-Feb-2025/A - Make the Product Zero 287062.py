# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

x = int(input()) 
a = list(map(int, input().split())) 


if 0 in a:
    print(0)
else:
    min_operations = min(abs(num) for num in a)
    print(min_operations)
