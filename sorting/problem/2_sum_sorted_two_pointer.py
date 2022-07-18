def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    i = 0
    j =len(numbers) - 1
    while i < j:
        _sum = numbers[i] + numbers[j]
        if _sum == target:
            return [i, j]
        elif _sum > target:
            j-=1
        else:
            i+=1
    return [-1,-1]


if __name__ == "__main__":
    print(pair_sum_sorted_array([-1,2,2,3,4,5], 8))