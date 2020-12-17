from typing import List

def threeSumClosest(nums: List[int], target: int) -> int:
    nums.sort()
    numsLengh = len(nums)
    closestTarget = 2 ** 31

    index2 = 1

    while(index2 < numsLengh - 1):

        index1 = 0
        index3 = numsLengh - 1
        while(index1 < index2 and index2 < index3):

            sum = nums[index1] + nums[index2] + nums[index3]

            if(sum == target):
                return target
            elif (abs(sum - target) < abs(closestTarget - target)):
                closestTarget = sum

            if(sum < target):
                index1 = index1 + 1

            elif(sum > target):
                index3 = index3 - 1

        index2 = index2 + 1

    return closestTarget

if __name__ == "__main__":
    print (threeSumClosest([-1,2,1,-4], 1), "expected 2")
    print (threeSumClosest([0,0,0,0], 0), "expected 0")
    print (threeSumClosest([-3,2,50,2], 100), "expected 54")
    print (threeSumClosest([0, 0, 3, 2], 0), "expected 2")
    print (threeSumClosest([1,2,4,8,16,32,64,128], 82), "expected 82")
