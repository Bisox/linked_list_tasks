from ListNode import ListNode, LinkedList

def double_remove(head: ListNode) -> ListNode:

    current = head
    

    while current is not None and current.next is not None:
        
        if current.val == current.next.val:
            current.next = current.next.next
            
        current = current.next
            
    return head




arr = [1, 2, 3, 3, 4, 5, 6]

head = LinkedList.create_linked_list(arr)
LinkedList.print_linked_list(head)