
def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    _hashmap = {}
    for i in range(0, len(numbers)):
        _second = target - numbers[i]
        if _second in _hashmap:
            return [_hashmap[_second], i]
        
        _hashmap[numbers[i]] = i
        
    return [-1,-1]

if __name__ == "__main__":
    print(two_sum([5, 3, 10, 45, 1], 6))