def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    for i in range(1, len(intervals)):
        if intervals[i][0] in range(intervals[i-1][0], intervals[i-1][1]):
            return 0
        
    return 1

if __name__ == "__main__":
    result = can_attend_all_meetings([[1,6], [1,3], [7,9]])
    print(result)