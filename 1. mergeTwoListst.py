from typing import Optional

from ListNode import ListNode, LinkedList

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    
    dummyNode = ListNode()
    current = dummyNode


    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            current.next = list1
            print(f'list1 = {list1}--->>>{list1.val} <= {list2.val}')
            list1 = list1.next
            

        else:
            current.next = list2
            print(f'list2 = {list2}--->>>{list1.val} >= {list2.val}')
            list2 = list2.next
            
        
        current = current.next

    current.next = list1 if list1 else list2


    return dummyNode.next 


arr1 = [1, 2, 3, 8, 10, 12]
arr2 = [1, 4, 6, 7, 8, 10]

linked_list1 = LinkedList.create_linked_list(arr1)
linked_list2 = LinkedList.create_linked_list(arr2)
head = mergeTwoLists(linked_list1, linked_list2)
LinkedList.print_linked_list(head)