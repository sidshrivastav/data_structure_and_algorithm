def subset(arr):
    _subset = []
    arr.sort()
    def helper(base, i=0, slate=[]):
        if i == len(base):
            _subset.append(slate[:])
            return

        count = 1
        j = i+1
        while j <= len(base)-1 and base[i] == base[j]:
            count+=1
            j+=1

        helper(base, i+count, slate)
        for k in range(1, count+1):
            helper(base, i+count, slate+([base[i]]*k))

    helper(arr)
    return _subset

if __name__ == "__main__":
    print(subset([1,2,2]))