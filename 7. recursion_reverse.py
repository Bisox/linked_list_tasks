from ListNode import ListNode, LinkedList

def recursion_reverse_linked_list(head: ListNode) -> ListNode:
    
    if head is None or head.next is None:
        return head
      
    new_head = recursion_reverse_linked_list(head.next)
    
    head.next.next = head 
    head.next = None
    
    return new_head



arr = [1, 2, 3, 3, 4, 5, 6]

linked_list = LinkedList.create_linked_list(arr)
head = recursion_reverse_linked_list(linked_list, 4)
LinkedList.print_linked_list(head)





