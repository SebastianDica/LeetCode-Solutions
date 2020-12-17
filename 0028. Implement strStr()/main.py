def strStr(haystack: str, needle: str) -> int:
    if (needle == ""):
        return 0

    locationIndex = -1

    haystackIndex = 0
    needleIndex = 0

    haystackLength = len(haystack)
    needleLength = len(needle)

    potentialNeedleStart = -1

    while haystackIndex < haystackLength:
        if(haystack[haystackIndex] == needle[needleIndex]):
            if potentialNeedleStart == -1:
                potentialNeedleStart = haystackIndex
            needleIndex = needleIndex + 1
            if needleLength == needleIndex:
                return potentialNeedleStart
        else:
            needleIndex = 0
            if potentialNeedleStart != -1:
                haystackIndex = potentialNeedleStart
            potentialNeedleStart = -1

        haystackIndex = haystackIndex + 1

    return locationIndex

if __name__ == "__main__":
    print (strStr("hello", "ll"), 2)
    print (strStr("aaaaa", "bba"), -1)
    print (strStr("aaaaa", "a"), 0)
    print (strStr("abcdefgz", "z"), 7)
    print (strStr("abcdefgz", "zh"), -1)
    print (strStr("abcdefgz", "fz"), -1)
    print (strStr("abdefgz", "abc"), -1)
    print (strStr("abdefgz", "e"), 3)
    print (strStr("abcdefg", "abcdefghlspo"), -1)
    print (strStr("", ""), 0)
    print (strStr("mississippi", "issip"), 4)
