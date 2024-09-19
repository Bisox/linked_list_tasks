from ListNode import ListNode, LinkedList


def reverse_linked_list(head: ListNode) -> ListNode:


    prev = None
    current = head

    while current:
        next_node = current.next

        current.next = prev

        prev = current

        current = next_node

    return prev



arr = [1, 2, 3, 4, 5, 6]

head = LinkedList.create_linked_list(arr)
LinkedList.print_linked_list(head)