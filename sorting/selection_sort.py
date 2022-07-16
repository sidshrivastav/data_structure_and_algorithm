def selection_sort(A: list) -> list:
    len_A = len(A)
    for i in range(0, len_A - 1):
        print("Selection for index {} \n".format(i))
        _min = A[i+1]
        _index = i+1
        for j in range(i+1, len_A):
            if A[j] < _min:
                _min = A[j]
                _index = j
        print("\tMinimum for remaining {} at index {} \n".format(_min, _index))
        if _min < A[i]:
            print("\t\tNeed Swap\n")
            A[i], A[_index] = A[_index], A[i]
        else:
            print("\t\tNo Swap needed.\n")
        print("\tUpdated Array: {}\n".format(A))
    
    print("Sorted: {}\n".format(A))
    return A


if __name__ == "__main__":
    selection_sort([7,9,8,1,3,2,6,5,10])