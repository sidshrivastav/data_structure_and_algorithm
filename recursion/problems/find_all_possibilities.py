from ssl import HAS_NEVER_CHECK_COMMON_NAME


def find_all_possibilities(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    _possibility = []
    def helper(S, i, slate=""):
        if i > len(S)-1:
           _possibility.append(slate)
           return

        if S[i] == "?":
            helper(S, i+1, slate+"1")
            helper(S, i+1, slate+"0")
        else:
            helper(S, i+1, slate+S[i]) 

    helper(s, 0)
    return _possibility

if __name__ == "__main__":
    print(find_all_possibilities("1?1?"))