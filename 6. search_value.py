from ListNode import ListNode, LinkedList

def search_value_into_linked_list(head: ListNode, value: int) -> bool:
    
    current = head

    while current is not None:
        if current.val == value:
            return True
        current = current.next

    return False

arr = [1, 2, 3, 3, 4, 5, 6]

linked_list = LinkedList.create_linked_list(arr)
head = search_value_into_linked_list(linked_list, 4)
LinkedList.print_linked_list(head)










