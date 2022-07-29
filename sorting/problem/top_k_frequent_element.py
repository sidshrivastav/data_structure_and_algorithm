import random
import collections

def top_k_frequent_element(arr, k):
    def helper(A, count_hash, start, end, index):
        if start == end:
            return

        pivot = random.randint(start, end)
        A[pivot], A[start] = A[start], A[pivot]
        i = start
        for j in range(start+1, end+1):
            if count_hash[A[j]] <= count_hash[A[start]]:
                i+=1
                A[i], A[j] = A[j], A[i]

        A[i], A[start] = A[start], A[i]

        if i == index:
            return
        elif index < i:
            helper(A, count_hash, start, i-1, index)
        else:
            helper(A, count_hash, i+1, end, index)  

    _h = collections.Counter(arr)
    unique = list(_h.keys())
    helper(unique, _h, 0, len(unique)-1, len(unique)-k)
    return unique[len(unique)-k:]

if __name__ == "__main__":
    a = top_k_frequent_element([5,3,1,1,1,3,73,1], 2)
    print(a)