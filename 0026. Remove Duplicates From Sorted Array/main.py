from typing import List

def removeDuplicates(nums: List[int]) -> int:
    newLength = 0
    oldLength = len(nums)

    if (oldLength == 0):
        return newLength

    index = 0
    previousNumber = None

    while index < oldLength:
        if previousNumber is None:
            previousNumber = nums[index]
            index = index + 1
            newLength = newLength + 1
        else:
            if nums[index] == previousNumber:
                nums[index:oldLength+1] = nums[index+1:oldLength+1]
                oldLength = oldLength - 1
            else:
                previousNumber = nums[index]
                index = index + 1
                newLength = newLength + 1

    return newLength

if __name__ == "__main__":
    print (removeDuplicates([1,1,2]), "expected 2")
    print (removeDuplicates([1,2,3]), "expected 3")
    print (removeDuplicates([1]), "expected 1")
    print (removeDuplicates([]), "expected 0")
    print (removeDuplicates([0,0,1,1,1,2,2,3,3,4]), "expected 5")
    longArray = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4]
    print (removeDuplicates(longArray), "expected 2")
    print (longArray)
