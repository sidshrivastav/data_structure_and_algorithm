class LinkedListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None
        
def merge_two_lists(list1, list2):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # time O(n+m), space: O(1)
    head = LinkedListNode(0)
    tail = head
    while list1 and list2:
        if list1.value < list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    tail.next = list1 if list2 is None else list2
    return head.next
    
def merge_k_lists(lists):
    """
    Args:
     lists(list_LinkedListNode_int32)
    Returns:
     LinkedListNode_int32
    """
    # time O(k(n+m)), space: O(1)
    if not len(lists):
        return None

    def helper(A, start, end):
        if start == end:
            return A[start]

        mid = (start + end)//2
        left = helper(A, start, mid)
        right = helper(A, mid+1, end)
        return merge_two_lists(left, right)
    
    return helper(lists, 0, len(lists)-1)


if __name__ == "__main__":
    first = LinkedListNode(2)
    first.next = LinkedListNode(8)
    first.next.next = LinkedListNode(12)

    second = LinkedListNode(3)
    second.next = LinkedListNode(3)
    second.next.next = LinkedListNode(5)
    second.next.next.next = LinkedListNode(13)

    third = LinkedListNode(1)
    third.next = LinkedListNode(3)
    third.next.next = LinkedListNode(7)
    third.next.next.next = LinkedListNode(15)

    result = merge_k_lists([first, second, third])
    while result is not None:
        print(result.value)
        result = result.next