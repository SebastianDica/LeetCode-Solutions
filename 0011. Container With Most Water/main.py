from typing import List

def maxArea(height: List[int]) -> int:
    leftEnd = 0
    rightEnd = len(height) - 1
    maxArea = 0

    while leftEnd != rightEnd:
        diff = rightEnd - leftEnd
        if height[leftEnd] <= height[rightEnd]:
            area = diff * height[leftEnd]
            leftEnd = leftEnd + 1
        else:
            area = diff * height[rightEnd]
            rightEnd = rightEnd - 1
        if(area > maxArea):
            maxArea = area

    return maxArea


if __name__ == "__main__":
    print (maxArea([1,8,6,2,5,4,8,3,7]), "expected 49")
    print (maxArea([10,100,100,2]), "expected 100")
    print (maxArea([1, 1]), "expected 1")
    print (maxArea([4, 3, 2, 1, 4]), "expected 16")
    print (maxArea([1, 2, 1]), "expected 2")
