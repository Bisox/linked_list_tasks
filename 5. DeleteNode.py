from ListNode import ListNode, LinkedList

def delete_node(head: ListNode, value: int):

    current = head

    if head is None:
        return head
    

    if value == head.val:
        current = head.next
        return current
        

    while current.next is not None:
        
        if current.next.val == value:
            current.next = current.next.next
            
                 
        current = current.next
    return head



arr = [1, 2, 3, 3, 4, 5, 6]

linked_list = LinkedList.create_linked_list(arr)
head = delete_node(linked_list, 4)
LinkedList.print_linked_list(head)