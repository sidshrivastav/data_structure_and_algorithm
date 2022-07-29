import random

def sort_array(arr):
    """
    Args:
     arr(list_char)
    Returns:
     list_char
    """
    def helper(A, start, end):
        if start >= end:
            return
        
        pivot = random.randint(start, end)
        A[start], A[pivot] = A[pivot], A[start]
        i = start
        for j in range(start+1, end+1):
            if ord(A[j]) <= ord(A[start]):
                i+=1
                A[i], A[j] = A[j], A[i]
                
        A[start], A[i] = A[i], A[start]
        
        helper(A, start, i-1)
        helper(A, i+1, end)
        
    helper(arr, 0, len(arr)-1)
    return arr
    

if __name__ == "__main__":
    a = sort_array(["a", "s", "d", "f", "g", "*", "&", "!", "z", "y"])
    print(a)