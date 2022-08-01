
from itertools import permutations


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

        for i in range(len(base)):
            helper(base[:i] + base[i+1:], slate+[base[i]])
    
    helper(arr)
    return _permutations


if __name__ == "__main__":
    print(get_permutations([0,1]))