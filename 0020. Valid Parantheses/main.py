def isValid(s: str) -> bool:
    stack = []

    openingBrackets = ["(", "[", "{"]
    closingBracketsMap = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    for character in s:
        if character in openingBrackets:
            stack.append(closingBracketsMap[character])
        else:
            if len(stack) > 0 and stack[len(stack) - 1] == character:
                stack.pop()
            else:
                return False

    return stack == []

if __name__ == "__main__":
    print (isValid(""), "expected true")
    print (isValid("()"), "expected true")
    print (isValid("()[]{}"), "expected true")
    print (isValid("(]"), "expected false")
    print (isValid("]"), "expected false")
    print (isValid("([)]"), "expected false")
    print (isValid("{[]}"), "expected true")
