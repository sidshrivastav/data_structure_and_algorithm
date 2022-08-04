def is_predecessor(w2, w1):
    # time: o(n) and space: o(1)
    if len(w2) != len(w1) + 1: return False
    i, j, extra = 0, 0, 0
    while i < len(w2) and j < len(w1):
        if w2[i] == w1[j]:
            i+=1
            j+=1
        else:
            i+=1
            extra+=1
    
    if i != len(w1)-1:
        extra = 1

    if extra == 1:
        return True

    return False


if __name__ == "__main__":
    print(is_predecessor("b", "a"))
    print(is_predecessor("bca", "bc"))
    print(is_predecessor("bda", "ba"))
    print(is_predecessor("bdaa", "ba"))