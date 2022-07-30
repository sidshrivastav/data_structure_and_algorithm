
import heapq

def kth_largest(k, initial_stream, append_stream):
    """
    Args:
     k(int32)
     initial_stream(list_int32)
     append_stream(list_int32)
    Returns:
     list_int32
    """
    arr = [float('-inf')] * k
    heapq.heapify(arr)
    for i in initial_stream:
        heapq.heappush(arr, i)
        heapq.heappop(arr)
    res = []
    for i in append_stream:
        heapq.heappush(arr, i)
        heapq.heappop(arr)
        res.append(arr[0])
    return res


if __name__ == "__main__":
    print(kth_largest(2, [4, 6], [5, 2, 20]))