def isValid(s: str) -> bool:
    if s == "()" or s == "[]" or s == "{}" or s == "":
        return True

    index = 0
    bracketCountOpen = 0
    bracketCountClosed = 0
    bracketType = s[index]

    if bracketType in [")", "]", "}"]:
        return False

    bracketTypeCloseMap = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    bracketTypeOpen = bracketType
    bracketTypeClose = bracketTypeCloseMap[bracketTypeOpen]

    while (index < len(s)):
        if s[index] == bracketTypeOpen:
            bracketCountOpen = bracketCountOpen + 1
        elif s[index] == bracketTypeClose:
            bracketCountClosed = bracketCountClosed + 1

        if bracketCountOpen == bracketCountClosed:
            return isValid(s[1:index]) and isValid(s[index+1:len(s)])

        index = index + 1

    return False

if __name__ == "__main__":
    print (isValid("()"), "expected true")
    print (isValid("()[]{}"), "expected true")
    print (isValid("(]"), "expected false")
    print (isValid("([)]"), "expected false")
    print (isValid("{[]}"), "expected true")
