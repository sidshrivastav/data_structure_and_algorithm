from bisect import bisect_left
 
def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1
    
def findDuplicate(nums):
    nums.sort()
    for i in range(0, len(nums)-1):
        _index = BinarySearch(nums[i+1:], nums[i])
        if _index != -1:
            return nums[_index + i]

if __name__ == "__main__":
    print(findDuplicate([1,3,4,2,2]))