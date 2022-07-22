
def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    numbers.sort()
    i = 0
    j = len(numbers)-1
    while i < j:
        if numbers[i]%2 == 0:
            i+=1
        elif numbers[j]%2 != 0:
            j-=1
        elif numbers[j]%2 == 0:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i+=1
                j-=1
        elif numbers[i]%2 != 0:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i+=1
                j-=1
    
    return numbers


if __name__ == "__main__":
    print(segregate_evens_and_odds([3,4,1,2,5,7,10,12]))