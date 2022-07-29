import heapq

def heapsort(arr):
    res = []
    heapq.heapify(arr)
    for _ in range(len(arr)):
        res.append(heapq.heappop(arr))
    return res

if __name__ == "__main__":
    print(heapsort([7,9,8,1,3,2,6,5,10]))