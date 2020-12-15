def isMatch(s: str, p: str) -> bool:

    stringLength = len(s)
    patternLength = len(p)

    if (stringLength == 0):
        if(patternLength == 0):
            return True
        else:
            return False
    else:
        if(patternLength == 0):
            return False

    stringIndex = 0
    patternIndex = 0

    while patternIndex < patternLength:
        if stringIndex >= stringLength:
            break
        if (patternIndex + 1 < patternLength):
            if p[patternIndex] == '.':
                if p[patternIndex + 1] == '*':
                    if patternIndex + 2 == patternLength:
                        return True
                    else:
                        endCharacter = p[patternIndex + 2]

                        while stringIndex < stringLength and s[stringIndex] != endCharacter:
                            stringIndex = stringIndex + 1

                        if(stringIndex >= stringLength):
                            return False

                        patternIndex = patternIndex + 2
                else:
                    stringIndex = stringIndex + 1
                    patternIndex = patternIndex + 1
            elif p[patternIndex].isalpha():
                if p[patternIndex + 1] == '*':
                    while stringIndex < stringLength and s[stringIndex] == p[patternIndex]:
                        stringIndex = stringIndex + 1
                    patternIndex = patternIndex + 2
                else:
                    if s[stringIndex] == p[patternIndex]:
                        stringIndex = stringIndex + 1
                        patternIndex = patternIndex + 1
                    else:
                        return False
        else:
            if p[patternIndex] == '.':
                stringIndex = stringIndex + 1
                patternIndex = patternIndex + 1
            elif p[patternIndex].isalpha():
                if s[stringIndex] == p[patternIndex]:
                    stringIndex = stringIndex + 1
                    patternIndex = patternIndex + 1
                else:
                    return False

    return True if stringIndex == stringLength and patternIndex == patternLength else False

if __name__ == "__main__":
    print (isMatch("aa", "a"), "expected False")
    print (isMatch("aa", "a*"), "expected True")
    print (isMatch("ab", ".*"), "expected True")
    print (isMatch("ab", "a.*"), "expected True")
    print (isMatch("ab", "a."), "expected True")
    print (isMatch("aab", "c*a*b"), "expected True")
    print (isMatch("ab", ".*c"), "expected False")
    print (isMatch("abc", ".*c"), "expected True")
    print (isMatch("mississippi", "mis*is*p*."), "expected False")
    print (isMatch("mississippi", "mis*is*ip*."), "expected True")
    print (isMatch("abc", ".*cc*"), "expected True")
    print (isMatch("abc", ".*c.*"), "expected True")
    print (isMatch("ab", ".*c.*"), "expected False")
    print (isMatch("aaa", "aaaa"), "expected False")
    print (isMatch("aaa", "a*a"), "expected True")
    print (isMatch("abcac", ".*c"), "expected True")
