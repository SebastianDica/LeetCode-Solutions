from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for index1, num1 in enumerate(nums):
        for index2, num2 in enumerate(nums):
            if (index1 != index2) and (num1 + num2) == target:
                return [index1, index2]

if __name__ == "__main__":
    print (twoSum([3, 2, 4], 6))
