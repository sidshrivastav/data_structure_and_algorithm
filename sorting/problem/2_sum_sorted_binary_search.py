from bisect import bisect_left
 
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    len_numbers = len(numbers)
    for i in range(0, len_numbers-1):
        _index = BinarySearch(numbers[i+1:], target-numbers[i])
        if _index > -1:
            return [i, i+_index+1]
            
    return [-1, -1]

if __name__ == "__main__":
    print(pair_sum_sorted_array([-1,2,2,3,4,5], 8))
    
