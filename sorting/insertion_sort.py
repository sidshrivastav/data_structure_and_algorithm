def insertion_sort(A: list) -> list:
    len_A = len(A)
    for i in range(0, len_A):
        print("{} pass\n".format(i+1))
        _temp = A[i]
        k = i
        while k > 0 and A[k-1] > _temp:
            A[k] = A[k-1]
            k=k-1
        A[k] = _temp
        print("\tUpdated Array: {}\n".format(A))
    print("Sorted: {}\n".format(A))
    return A


if __name__ == "__main__":
    insertion_sort([7,9,8,1,3,2,6,5,10])