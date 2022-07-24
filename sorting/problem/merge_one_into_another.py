def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    second_copy = second[:len(first)]
    i = 0
    j = 0
    k = 0
    while i < len(first) and j < len(second_copy):
        if first[i] <= second_copy[j]:
            second[k] = first[i]
            i+=1
            k+=1
        else:
            second[k] = second_copy[j]
            j+=1
            k+=1

    if i < len(first):
        while i < len(first):
            second[k] = first[i]
            i+=1
            k+=1

    if j < len(second_copy):
        while j < len(second_copy):
            second[k] = second_copy[j]
            j+=1
            k+=1
            

    return second



if __name__ == "__main__":
    result = merge_one_into_another([6,8,10], [4,5,7,0,0,0])
    print(result)