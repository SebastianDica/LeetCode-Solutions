import math

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False

    surgeryX = x
    y = 0

    while surgeryX >= 10:
        y = y * 10 + (surgeryX % 10)
        surgeryX = math.floor(surgeryX / 10)

    y = y * 10 + surgeryX

    return x == y

if __name__ == "__main__":
    print (isPalindrome(121), "expected True")
    print (isPalindrome(313), "expected True")
    print (isPalindrome(-121), "expected False")
    print (isPalindrome(10), "expected False")
    print (isPalindrome(-101), "expected False")
