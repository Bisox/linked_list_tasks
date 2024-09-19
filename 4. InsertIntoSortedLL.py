from ListNode import ListNode, LinkedList

def insert_into_sorted_list(head: ListNode, val: int) -> ListNode:
    
    new_node = ListNode(val)

    
    if head is None:
        return new_node

    
    if val < head.val:
        new_node.next = head
        return new_node

    
    current = head
    while current.next is not None:
        if current.val < val < current.next.val:
            new_node.next = current.next
            current.next = new_node
            return head  
        
        current = current.next

    
    current.next = new_node
    return head


arr = [1, 2, 3, 5, 6]

linked_list = LinkedList.create_linked_list(arr)
head = insert_into_sorted_list(linked_list, 0)
LinkedList.print_linked_list(head)