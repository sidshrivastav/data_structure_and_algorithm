
def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    _combinations = []
    def helper(base, i=0, slate = []):
        if len(slate) == k:
            _combinations.append(slate[:])
            return
        if i >= len(base):
            return
        helper(base, i+1, slate)
        helper(base, i+1, slate+[base[i]])
    
    n_arr = []
    for i in range(1, n+1):
        n_arr.append(i)
    helper(n_arr)
    return _combinations


if __name__ == "__main__":
    print(find_combinations(5, 2))