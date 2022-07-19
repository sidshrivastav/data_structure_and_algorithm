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
        
    for i in range(1, len(lists)):
        lists[0] = merge_two_lists(lists[0], lists[1])
    return lists[0]
