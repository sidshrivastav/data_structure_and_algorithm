
def three_sum(numbers):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    res = []
    for i in range(0, len(numbers)):
        _second = 0 - numbers[i]
        _hashmap = {}
        for j in range(i+1, len(numbers)):
            _third = _second - numbers[j]
            if _third in _hashmap:
                if i!=j and j!=_hashmap[_third] and i!=_hashmap[_third]:
                    founded_triplets = sorted([numbers[i], numbers[j], _third])
                    if founded_triplets not in res:
                        res.append(founded_triplets)
        
            _hashmap[numbers[j]] = j
        
    return res

if __name__ == "__main__":
    print(three_sum([-1,0,1,2,-1,-4]))