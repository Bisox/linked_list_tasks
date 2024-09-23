from ListNode import ListNode, LinkedList

def double_remove(head: ListNode) -> ListNode:

    current = head
    

    while current is not None and current.next is not None:
        
        if current.val == current.next.val:
            current.next = current.next.next
            
        current = current.next
            
    return head




arr = [1, 1, 2, 3, 3, 4, 5, 6, 6]

linked_list = LinkedList.create_linked_list(arr)
head = double_remove(linked_list)
LinkedList.print_linked_list(head)