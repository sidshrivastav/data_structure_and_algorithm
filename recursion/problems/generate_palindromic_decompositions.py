def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    _decomposition = []
    def helper(S, i=0, slate=[]):
        if i == len(S):
            correct = True
            for j in slate:
                if j != j[::-1]:
                    correct = False
                    break
            
            if correct:
                _decomposition.append("|".join(slate))
            return

        slate.append(S[i])
        helper(S, i+1, slate)
        slate.pop()
        if len(slate):
            slate[-1]+=S[i]
            helper(S, i+1, slate)
            slate[-1] = slate[-1][:-1]

    helper(s, 0, [])
    return _decomposition    


if __name__ == "__main__":
    print(generate_palindromic_decompositions("aad"))