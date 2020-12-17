from typing import List

def removeElement(nums: List[int], val: int) -> int:
    newLength = 0
    oldLength = len(nums)

    index = 0

    while index < oldLength:
        if nums[index] == val:
            nums[index:oldLength + 1] = nums[index+1:oldLength+1]
            oldLength = oldLength - 1
        else:
            index = index + 1
            newLength = newLength + 1

    return newLength

if __name__ == "__main__":
    testList = [3,2,2,3]
    print (removeElement(testList, 3), testList, " expected 2 , [2,2]")
    testList = [3,2,2,3]
    print (removeElement(testList, 4), testList, " expected 4 , [3,2,2,3]")
    testList = []
    print (removeElement(testList, 4), testList, " expected 0 , []")
    testList = [0,1,2,2,3,0,4,2]
    print (removeElement(testList, 2), testList, " expected 5 , [0,1,4,0,3]")
