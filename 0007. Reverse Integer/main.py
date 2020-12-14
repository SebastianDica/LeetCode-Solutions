import math

def reverse(x: int) -> int:
    negative = x < 0
    if (negative):
        x = x * (-1)
    reversed = 0
    maxInteger = (2 ** 31) - 1

    while x >= 10:
        remainder = x % 10
        reversed = reversed * 10 + remainder
        x = math.floor(x / 10)

    reversed = reversed * 10 + x
    reversed = reversed * (-1) if negative else reversed

    return 0 if reversed >= maxInteger or reversed <= (-1) * maxInteger else reversed

if __name__ == "__main__":
    print (reverse(123), "expected 321")
    print (reverse(-123), "expected -321")
    print (reverse(120), "expected 21")
    print (reverse(10), "expected 1")
    print (reverse(-120), "expected -21")
    print (reverse(0), "expected 0")
    print (reverse(2147483646), "expected 0")
