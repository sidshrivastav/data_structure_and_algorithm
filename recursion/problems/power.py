_hash = {}

def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    one = b // 2
    second = b - one
    if one in _hash:
        _one = _hash[one]
    else:
        _one = power(a, one)
        _hash[one] = _one

    if second in _hash:
        _second = _hash[second]
    else:
        _second = power(a, second)
        _hash[second] = _second

    return (_one * _second)%1000000007

#1000000000000000000
if __name__ == "__main__":
    print(power(10000000,10000000))