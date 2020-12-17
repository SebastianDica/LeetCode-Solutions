class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    finalHead = None
    itermediaryList = None

    while l1 != None or l2 != None:
        if l1 != None and l2 != None:
            winner = l1.val

            if l1.val > l2.val:
                winner = l2.val
                l2 = l2.next
            else:
                l1 = l1.next

            if itermediaryList == None:
                itermediaryList = ListNode(winner)
                finalHead = itermediaryList
            else:
                itermediaryList.next = ListNode(winner)
                itermediaryList = itermediaryList.next

        elif l1 != None:
            if itermediaryList == None:
                finalHead = l1
            else:
                itermediaryList.next = l1
            l1 = None
        elif l2 != None:
            if itermediaryList == None:
                finalHead = l2
            else:
                itermediaryList.next = l2
            l2 = None

    return finalHead

if __name__ == "__main__":
    listNode = mergeTwoLists(
            ListNode(1, ListNode(2, ListNode(4))),
            ListNode(1, ListNode(3, ListNode(4)))
        )

    print (listNode.val, "expected 1")
    print (listNode.next.val, "expected 1")
    print (listNode.next.next.val, "expected 2")
    print (listNode.next.next.next.val, "expected 3")
    print (listNode.next.next.next.next.val, "expected 4")
    print (listNode.next.next.next.next.next.val, "expected 4")
    print (listNode.next.next.next.next.next.next, "expected None")

    listNode = mergeTwoLists(
            None,
            None
        )

    print (listNode, "expected None")

    listNode = mergeTwoLists(
            None,
            ListNode(0)
        )

    print (listNode.val, "expected 0")
    print (listNode.next, "expected None")
