from ListNode import ListNode, LinkedList


def search_middle_element(head: ListNode):

    slow = head
    fast = head
    while fast and fast.next and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow.val
    


arr = [1, 2, 3, 4, 5]

linked_list = LinkedList.create_linked_list(arr)
head = search_middle_element(linked_list)
print(head)
