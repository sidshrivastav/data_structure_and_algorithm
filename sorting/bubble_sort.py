def bubble_sort(A: list) -> list:
    len_A = len(A)
    for k in range(0, len_A - 2):
        print("Pass {}\n".format(k+1))
        for i in range(1, (len_A - 1 - k)):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
            print("\t{}: {}".format(i, A))
        print("\n")
    print("Sorted: {}\n".format(k+1))
    return A

if __name__ == "__main__":
    bubble_sort([7,9,8,1,3,2,6,5,10])