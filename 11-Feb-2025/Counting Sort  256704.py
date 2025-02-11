# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem


def countingSort(arr):
    
    store = [0] * (100)
    
    for num in arr:
        store[num] += 1
    
    
    return store
