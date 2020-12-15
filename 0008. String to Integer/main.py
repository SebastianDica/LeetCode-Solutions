def myAtoi(s: str) -> int:
    result = 0
    negated = False
    digitRecorded = False
    digitExpected = False
    invalid = False
    maxInteger = (2 ** 31) - 1
    minInteger = (-1) * (2 ** 31)

    for character in s:
        if digitRecorded is False:
            if digitExpected is True and not character.isdigit():
                invaid = True
                break
            if character is ' ':
                pass
            elif character is '-':
                negated = not negated
                digitExpected = True
            elif character is '+':
                digitExpected = True
                pass
            elif character.isdigit():
                result = result * 10 + int(character)
                digitRecorded = True
            else:
                invalid = True
                break
        else:
            if character.isdigit():
                result = result * 10 + int(character)
            else:
                break

    if invalid is True:
        return 0

    result = result * (-1) if negated else result
    result = result if result < maxInteger else maxInteger
    result = result if result > minInteger else minInteger
    return result

if __name__ == "__main__":
    print (myAtoi("=-12"), "expected 0")
    print (myAtoi("42"), "expected 42")
    print (myAtoi("0"), "expected 0")
    print (myAtoi("0 is a number too"), "expected 0")
    print (myAtoi("+42"), "expected 42")
    print (myAtoi("             -42"), "expected -42")
    print (myAtoi("4193 with words"), "expected 4193")
    print (myAtoi("4193- with words"), "expected 4193")
    print (myAtoi("words and 987"), "expected 0")
    print (myAtoi("-91283472332"), "expected -2147483648")
    print (myAtoi("21474836460"), "expected 2147483647")
