def get_permutations(arr):
    """
    Args
     arr(list_int32)
    Returns:
     list_list_int32
    """
    _permutations = []
    def helper(base, slate=[]):
        if len(base) == 0:
            _permutations.append(slate)
            return
        _temp = []
        for i in range(len(base)):
            if base[i] not in _temp:
                helper(base[:i] + base[i+1:], slate+[base[i]])
                _temp.append(base[i])
            
    
    helper(arr)
    return _permutations


if __name__ == "__main__":
    print(get_permutations([1,1,2]))