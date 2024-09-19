from ListNode import ListNode, LinkedList








arr = [1, 2, 3, 3, 4, 5, 6]

linked_list = LinkedList.create_linked_list(arr)
head = recursion_reverse_linked_list(linked_list, 4)
LinkedList.print_linked_list(head)