from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper functions for testing
def fromList(list: List[int]) -> ListNode:
    if len(list) == 0:
        return None
    else:
        return ListNode(list[0], fromList(list[1:len(list)]))

def fromLists(lists: List[List[int]]) -> List[ListNode]:
    finalList = []
    for list in lists:
        finalList.append(fromList(list))
    return finalList

def printListNode(listNode: ListNode):
    result = ""
    if (listNode is None):
        return "[]"
    while listNode is not None:
        result = result + str(listNode.val) + ("->" if listNode.next is not None else "")
        listNode = listNode.next
    return result

# Actual code
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    finalHead = None
    previousNode = None
    nextNode = None

    if k == 1:
        return head

    while head is not None:
        intermediaryKList = None
        intermediaryKListTail = None
        intermediaryKListAux = None
        kIndex = 0
        while kIndex < k:
            if head is not None:
                if intermediaryKList is None:
                    intermediaryKList = head
                    intermediaryKListAux = head
                    intermediaryKListTail = head
                else:
                    intermediaryKListAux.next = head
                    intermediaryKListTail = head
                    intermediaryKListAux = intermediaryKListAux.next
                head = head.next
            else:
                if (finalHead is None):
                    finalHead = intermediaryKList
                else:
                    previousNode.next = intermediaryKList
                return finalHead
            kIndex = kIndex + 1

        nextNode = intermediaryKListAux
        intermediaryKListTail.next = None
        (reversedListHead, reversedListTail) = reverseList(intermediaryKList)
        if (finalHead is None):
            finalHead = reversedListHead
        else:
            if previousNode is not None:
                previousNode.next = reversedListHead
            else:
                previousNode = reversedListHead
        previousNode = reversedListTail

    return finalHead

def reverseList(head: ListNode) -> (ListNode, ListNode):
    if head is None:
        return (None, None)
    if head.next is None:
        return (head, None)

    (reversedListHead, reversedListTail) = reverseList(head.next)

    if reversedListTail is not None:
        reversedListTail.next = head
        head.next = None
        reversedListTail = reversedListTail.next
    else:
        reversedListTail = head
        head.next = None
        reversedListHead.next = reversedListTail

    return (reversedListHead, reversedListTail)

if __name__ == "__main__":
    print (printListNode(reverseKGroup(fromList([1,2,3,4,5]), 4
        )), " expected 4->3->2->1->5")
    print (printListNode(reverseKGroup(fromList([1,2,3,4,5]), 2
        )), " expected 2->1->4->3->5")
    print (printListNode(reverseKGroup(fromList([1,2,3,4,5]), 3
        )), " expected 3->2->1->4->5")
    print (printListNode(reverseKGroup(fromList([1,2,3,4,5,6]), 3
        )), " expected 3->2->1->6->5->4")
    print (printListNode(reverseKGroup(fromList([1,2,3,4,5]), 1
        )), " expected 1->2->3->4->5")
    print (printListNode(reverseKGroup(fromList([1]), 1
        )), " expected 1")
