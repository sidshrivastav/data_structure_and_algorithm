def subset(arr):
    _subset = []
    def helper(base, i=0, slate=[]):
        if i == len(base):
            _subset.append(slate[:])
            return
        helper(base, i+1, slate)
        helper(base, i+1, slate+[base[i]])
    helper(arr)
    return _subset

if __name__ == "__main__":
    print(subset([1,2,3]))