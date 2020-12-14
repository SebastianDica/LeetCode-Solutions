from typing import List
import math

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)

    total = m + n

    even = total % 2 == 0
    halfPoint = total / 2
    expectedMedianIndeces = [math.floor(halfPoint)] if not even else [halfPoint - 1, halfPoint]

    indexM = 0
    indexN = 0

    selectedMedians = []

    while indexN < n or indexM < m:
        if (len(selectedMedians) == len(expectedMedianIndeces)):
            break

        selectedValue = None

        if indexN < n and indexM < m:
            if( nums1[indexM] > nums2[indexN] ):
                selectedValue = nums2[indexN]
                indexN = indexN + 1
            else:
                selectedValue = nums1[indexM]
                indexM = indexM + 1
        elif indexN < n:
            selectedValue = nums2[indexN]
            indexN = indexN + 1
        elif indexM < m:
            selectedValue = nums1[indexM]
            indexM = indexM + 1

        if ((indexM + indexN - 1) in expectedMedianIndeces and selectedValue is not None):
            selectedMedians.append(selectedValue)

    if (len(selectedMedians) > 0):
        return sum(selectedMedians) / len(selectedMedians)
    else:
        return 0.0

if __name__ == "__main__":
    print (findMedianSortedArrays([1,3], [2]), "expected 2")
    print (findMedianSortedArrays([2,2,2], [2,2,2]), "expected 2")
    print (findMedianSortedArrays([2,3,4], [2,3,4]), "expected 3")
    print (findMedianSortedArrays([1,2], [3,4]), "expected 2.5")
    print (findMedianSortedArrays([1,2,3], [10,11,12]), "expected 6.5")
    print (findMedianSortedArrays([10,11,12], [1,2,3]), "expected 6.5")
    print (findMedianSortedArrays([], [2]), "expected 2")
    print (findMedianSortedArrays([2], []), "expected 2")
    print (findMedianSortedArrays([1], [2]), "expected 1.5")
    print (findMedianSortedArrays([], []), "expected 0? maybe")
