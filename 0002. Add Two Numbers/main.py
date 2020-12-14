class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    return count(l1, l2, 0)

def count(l1: ListNode, l2: ListNode, remainder: int) -> ListNode:
    if(l1 == None and l2 == None):
        if(remainder > 0):
            return ListNode(remainder)
        else:
            return None

    l1Val = 0
    l2Val = 0
    l1Next = None
    l2Next = None

    if(l1 != None):
        l1Val = l1.val
        l1Next = l1.next
    if(l2 != None):
        l2Val = l2.val
        l2Next = l2.next

    sum = l1Val + l2Val + remainder
    remainder = 0

    if(sum >= 10):
       remainder = 1
       sum = sum % 10

    return ListNode(sum, count(l1Next, l2Next, remainder))

if __name__ == "__main__":
    listNode = addTwoNumbers(
            ListNode(9, ListNode(9, ListNode(9))),
            ListNode(9, ListNode(9))
        )

    print (listNode.val)
    print (listNode.next.val)
    print (listNode.next.next.val)
    print (listNode.next.next.next.val)
