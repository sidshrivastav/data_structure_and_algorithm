
def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    _permutation = []
    def helper(base, _index, slate=""):
        if _index > len(base) - 1:
            _permutation.append(slate)
            return
        
        if base[_index].isnumeric():
            helper(base, _index+1, slate+base[_index])
        else:
            helper(base, _index+1, slate+base[_index].upper())
            helper(base, _index+1, slate+base[_index].lower())

    helper(s, 0)
    return _permutation

if __name__ == "__main__":
    print(letter_case_permutations("123"))