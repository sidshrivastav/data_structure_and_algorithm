from numpy import append


def find_intersection(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    i, j, k = 0, 0, 0
    intersections = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] and arr1[i] == arr3[k] and arr2[j] == arr3[k]:
            intersections.append(arr1[i])
            i+=1
            j+=1
            k+=1
        else:
            if arr1[i] < arr2[j] or arr1[i] < arr3[k]:
                i+=1
            elif arr2[j] < arr1[i] or arr2[j] < arr3[k]:
                j+=1
            elif arr3[k] < arr1[i] or arr3[k] < arr2[j]:
                k+=1
    
    return intersections if len(intersections) > 0 else -1

if __name__ == "__main__":
    print(find_intersection([1, 2, 2, 2, 9], [1, 1, 2, 2], [1, 1, 1, 2, 2, 2]))
