import random

def quick_select(arr, k):
    def helper(A, start, end, index):
        if start == end:
            return

        pivot = random.randint(start, end)
        A[pivot], A[start] = A[start], A[pivot]
        i = start
        for j in range(start+1, end+1):
            if A[j] <= A[start]:
                i+=1
                A[i], A[j] = A[j], A[i]

        A[i], A[start] = A[start], A[i]

        if i == index:
            return
        elif index < i:
            helper(arr, start, i-1, index)
        else:
            helper(arr, i+1, end, index)  

    helper(arr, 0, len(arr)-1, len(arr)-k)
    return arr[len(arr)-k]

if __name__ == "__main__":
    a = quick_select([7,9,8,1,3,2,6,5,10], 3)
    print(a)