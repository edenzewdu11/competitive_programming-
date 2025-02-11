# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    n = len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]: 
            arr[j+1]=arr[j]
            j-=1
            print(*arr)
    arr[j+1]=key
    print(*arr)
