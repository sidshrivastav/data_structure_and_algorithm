def merge_sort(arr):
    def helper(A, start, end):
        # leaf worker
        if start == end:
            return A[start]

        # Internal worker
        mid = (start + end)//2
        helper(A, start, mid)
        helper(A, mid+1, end)

        # Merging sorted array
        i = start
        j = mid+1
        aux = []
        while i <= mid and j <= end:
            if A[i] <= A[j]:
                aux.append(A[i])
                i+=1
            else:
                aux.append(A[j])
                j+=1
        while i <= mid:
            aux.append(A[i])
            i+=1
        while j <= end:
            aux.append(A[j])
            j+=1

        A[start: end+1] = aux
        
    helper(arr, 0, len(arr)-1)
    return arr

if __name__ == "__main__":
    a = merge_sort([7,9,8,1,3,2,6,5,10])
    print(a)