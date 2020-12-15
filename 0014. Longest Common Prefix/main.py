from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    common = ""

    if len(strs) == 0:
        return common

    minLength = 2**31
    for str in strs:
        print(str)
        if len(str) < minLength:
            minLength = len(str)

    index = 0

    print(minLength)
    while (index < minLength):
        base = strs[0][index]
        for str in strs:
            if (str[index] != base):
                return common
        common = common + base
        index = index + 1

    return common

if __name__ == "__main__":
    print (longestCommonPrefix(["flower","flow","flight"]), "expected fl")
    print (longestCommonPrefix(["flower","flow"]), "expected flow")
    print (longestCommonPrefix(["",""]), "expected ")
    print (longestCommonPrefix(["dog","racecar","car"]), "expected ")
    print (longestCommonPrefix(["dog","racecar","race"]), "expected ")
