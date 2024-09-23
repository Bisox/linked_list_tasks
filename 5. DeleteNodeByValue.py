from ListNode import ListNode, LinkedList

def delete_element_by_value(head: ListNode, value: int) -> ListNode | None:

    if head is None:
        return None


    if head.val == value:
        return head.next

    current = head

    

    while current.next is not None:

        if current.next.val == value:
            current.next = current.next.next
            return head
        
        current = current.next

    return head


arr = [1, 2, 3, 3, 4, 5, 6]

linked_list = LinkedList.create_linked_list(arr)
head = delete_element_by_value(linked_list, 4)
LinkedList.print_linked_list(head)