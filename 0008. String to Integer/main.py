from typing import List

def myAtoi(s: str) -> int:
    return 0

if __name__ == "__main__":
    print (myAtoi("42"), "expected 42")
    print (myAtoi("+42"), "expected 42")
    print (myAtoi("             -42"), "expected -42")
    print (myAtoi("4193 with words"), "expected 4193")
    print (myAtoi("words and 987"), "expected 0")
    print (myAtoi("-91283472332"), "expected -2147483648")
