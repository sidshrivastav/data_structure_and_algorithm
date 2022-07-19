class LinkedListNode:
    def __init__(self, value=0):
        self.value = value
        self.next = None

def merge_2_sorted_linked_list(first, second):
    head = LinkedListNode()
    tail = head
    while first and second:
        if first.value < second.value:
            tail.next = first
            first = first.next
        else:
            tail.next = second
            second = second.next

        tail = tail.next
    
    tail.next = second if first is None else first
    return head.next
            


if __name__ == "__main__":
    first = LinkedListNode(2)
    # first.next = LinkedListNode(8)
    # first.next.next = LinkedListNode(12)

    second = LinkedListNode(3)
    # second.next = LinkedListNode(3)
    # second.next.next = LinkedListNode(5)
    # second.next.next.next = LinkedListNode(13)

    result = merge_2_sorted_linked_list(first, second)
    while result is not None:
        print(result.value)
        result = result.next
