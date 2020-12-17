# Attempt 2, unsuccesful so far

def isMatch(s: str, p: str) -> bool:
    stringLength = len(s)
    patternLength = len(p)

    if (stringLength == 0 and patternLength == 0):
        return True
    if (stringLength != 0 and patternLength == 0):
        return False

    stringIndex = 0
    patternIndex = 0
    emptyString = stringLength == 0

    if (patternIndex + 1 < patternLength):
        if p[patternIndex] == '.':
            if p[patternIndex + 1] == '*':
                return isMatch(s, p[2:patternLength]) or (isMatch(s[1:stringLength], p) or isMatch(s[1:stringLength], p[2:patternLength])
                    if not emptyString else False)
            else:
                return isMatch(s[1:stringLength], p[1:patternLength]) if not emptyString else False
        elif p[patternIndex].isalpha():
            if p[patternIndex + 1] == '*':
                return isMatch(s, p[2:patternLength]) or (isMatch(s[1:stringLength], p) or isMatch(s[1:stringLength], p[2:patternLength])
                    if not emptyString and s[stringIndex] == p[patternIndex] else False)
            else:
                return isMatch(s[1:stringLength], p[1:patternLength]) if not emptyString and s[stringIndex] == p[patternIndex] else False

    if p[patternIndex] == '.':
        return isMatch(s[1:stringLength], p[1:patternLength]) if not emptyString else False
    elif p[patternIndex].isalpha():
        return isMatch(s[1:stringLength], p[1:patternLength]) if not emptyString and s[stringIndex] == p[patternIndex] else False


if __name__ == "__main__":
    # print (isMatch("aa", "a"), "expected False")
    # print (isMatch("aa", "a*"), "expected True")
    # print (isMatch("ab", ".*"), "expected True")
    # print (isMatch("ab", "a.*"), "expected True")
    # print (isMatch("ab", "a."), "expected True")
    # print (isMatch("aab", "c*a*b"), "expected True")
    # print (isMatch("ab", ".*c"), "expected False")
    # print (isMatch("abc", ".*c"), "expected True")
    # print (isMatch("ab", ".*c.*"), "expected False")
    # print (isMatch("aaa", "aaaa"), "expected False")
    # print (isMatch("aaa", "a*a"), "expected True")
    # print (isMatch("aaa", "a*aa*a"), "expected True")
    # print (isMatch("abcac", ".*c"), "expected True")
    # print (isMatch("abc", ".*cc*"), "expected True")
    # print (isMatch("abc", ".*c.*"), "expected True")
    # print (isMatch("mississippi", "mis*is*p*."), "expected False")
    # print (isMatch("mississippi", "mis*is*ip*."), "expected True")
    # print (isMatch("a", ".*..a*"), "expected False")
    print (isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
