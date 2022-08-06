def pivotArray(nums, pivot):
    pi = nums.index(pivot)
    nums[0], nums[pi] = nums[pi], nums[0]
    i = 0
    for j in range(1, len(nums)):
        if nums[j] <= nums[0]:
            i+=1
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[i], nums[0] = nums[0], nums[i]
    return nums

if __name__ == "__main__":
    print(pivotArray([9,12,5,10,14,3,10], 10))