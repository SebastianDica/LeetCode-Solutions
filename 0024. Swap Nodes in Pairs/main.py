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
def swapPairs(head: ListNode) -> ListNode:
    finalHead = None
    savedStart = False
    previousNode = None

    while head is not None:
        if head.next is not None:
            nextHead = head.next
            listRemainder = nextHead.next
            nextHead.next = head
            head.next = listRemainder

            if previousNode is not None:
                previousNode.next = nextHead

            previousNode = head
            head = listRemainder

            if savedStart is False:
                savedStart = True
                finalHead = nextHead
        else:
            if savedStart is False:
                savedStart = True
                finalHead = head
            head = head.next

    return finalHead

if __name__ == "__main__":
    print (printListNode(swapPairs(fromList([1,2,3,4])
        )), " expected 2->1->4->3")
    print (printListNode(swapPairs(fromList([1,2,3,4,5])
        )), " expected 2->1->4->3->5")
    print (printListNode(swapPairs(fromList([1,2,3,4,5,6,7])
        )), " expected 2->1->4->3->6->5->7")
    print (printListNode(swapPairs(fromList([1,2,3,4,5,6,7,8])
        )), " expected 2->1->4->3->6->5->8->7")
    print (printListNode(swapPairs(fromList([])
        )), " expected []")
    print (printListNode(swapPairs(fromList([1])
        )), " expected 1")
