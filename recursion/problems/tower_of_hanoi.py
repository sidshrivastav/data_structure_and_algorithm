def tower_of_hanoi(t):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    _moves = []
    def helper(n, src, dst, aux):
        if n == 1:
            _moves.append([src, dst])
            return
        
        helper(n-1, src, aux, dst)
        _moves.append([src, dst])
        helper(n-1, aux, dst, src)

    helper(t, 1, 3, 2)
    return _moves


if __name__ == "__main__":
    print(tower_of_hanoi(4))
