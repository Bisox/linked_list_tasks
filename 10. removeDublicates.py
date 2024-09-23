from ListNode import ListNode, LinkedList

# **Удаление дубликатов**:
#     - Удалить все дубликаты из отсортированного связного списка.
#     - Удалить все дубликаты из неотсортированного связного списка


def remove_doubliсates_element_sorted(head: ListNode):
    


    current = head

    while current and current.next:
        if current.val == current.next.val:
            
            current.next = current.next.next
        else:
            
            current = current.next

    return head




def remove_duplicates_unsorted(head: ListNode) -> ListNode:
    if not head:
        return None

    seen = set()
    current = head
    seen.add(current.val)

    while current and current.next:
        if current.next.val in seen:
            
            current.next = current.next.next
        else:
            
            seen.add(current.next.val)
            current = current.next

    return head



arr = [1, 4, 4, 1, 1, 2, 3, 3, 3, 3, 4, 5, 6, 6, 6]

linked_list = LinkedList.create_linked_list(arr)
head = remove_duplicates_unsorted(linked_list)
LinkedList.print_linked_list(head)