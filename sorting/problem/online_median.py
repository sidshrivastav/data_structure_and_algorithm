import heapq
import math

def online_median(stream):
    """
    Args:
     stream(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    _min_heap = []
    _max_heap = []
    heapq.heapify(_min_heap)
    heapq.heapify(_max_heap)
    median = 0.0
    res = []
    for i in stream:
        if i > median:
            heapq.heappush(_min_heap, i)
            if len(_min_heap) - len(_max_heap) == 2:
                t = heapq.heappop(_min_heap)
                heapq.heappush(_max_heap, t*(-1))
        else:
            heapq.heappush(_max_heap, i*(-1))
            if len(_max_heap) - len(_min_heap) == 2:
                t = heapq.heappop(_max_heap)
                t = t*(-1)
                heapq.heappush(_min_heap, t)

        if len(_max_heap) == len(_min_heap):
            median = (_min_heap[0] + (-1*(_max_heap[0])))/2
        elif len(_max_heap) > len(_min_heap):
            median = -1*_max_heap[0]
        else:
            median = _min_heap[0]

        res.append(math.floor(median))

    return res

if __name__ == "__main__":
    print(online_median( [4, 3, 2, 1]))