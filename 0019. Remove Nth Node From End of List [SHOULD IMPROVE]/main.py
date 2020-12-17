class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Could you do this in one pass?

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    return removeNth(head, listLength(head) - n)

def removeNth(head: ListNode, n: int) -> ListNode:
    if head == None:
        return None

    if n == 0:
        if head is not None:
            return head.next
        else:
            return None

    head.next = removeNth(head.next, n - 1)
    return head

def listLength(head: ListNode) -> int:
    if head is None:
        return 0
    else:
        return 1 + listLength(head.next)

if __name__ == "__main__":
    listNode = removeNthFromEnd(
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            2
        )

    print (listNode.val, "expected 1")
    print (listNode.next.val, "expected 2")
    print (listNode.next.next.val, "expected 3")
    print (listNode.next.next.next.val, "expected 5")

    listNode = removeNthFromEnd(
            ListNode(1),
            1
        )

    print (listNode, "expected None")

    listNode = removeNthFromEnd(
            ListNode(1, ListNode(2)),
            1
        )

    print (listNode.val, "expected 1")
