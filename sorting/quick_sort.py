import random

def partition(A, start, end):
    pivot = random.randint(start, end) 
    A[pivot], A[start] = A[start], A[pivot]
    orange = start
    for green in range(start+1, end+1):
        if A[green] <= A[start]:
            orange+=1
            A[orange], A[green] = A[green], A[orange]
            
    A[orange], A[start] = A[start], A[orange]
    return orange

def quick_sort(arr, start, end):
    if start < end:
        # Internal worker
        p = partition(arr, start, end)
        quick_sort(arr, start, p-1)
        quick_sort(arr, p+1, end)  
        return arr
    return arr

if __name__ == "__main__":
    a = quick_sort([7,9,8,1,3,2,6,5,10], 0, 8)
    print(a)