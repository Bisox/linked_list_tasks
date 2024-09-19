from ListNode import ListNode, LinkedList

def has_cicle(head: ListNode) -> bool:

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


        if slow == fast:
            return True
        
    return False


arr = [1, 2, 3, 3, 4, 5, 6]

linked_list = LinkedList.create_linked_list(arr)
head = has_cicle(linked_list)
LinkedList.print_linked_list(head)





