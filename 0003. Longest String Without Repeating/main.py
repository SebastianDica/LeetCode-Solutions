def lengthOfLongestSubstring(s: str) -> int:
    maxLength = 0

    itermediaryCharMap = {}
    itermediaryLength = 0

    index = 0

    while index < len(s):
       if (itermediaryLength > maxLength):
           maxLength = itermediaryLength

       character = s[index]

       if character in itermediaryCharMap.keys():
           index = itermediaryCharMap[character] + 1
           del itermediaryCharMap[character]
           itermediaryLength = 0
       else:
           itermediaryCharMap[character] = index
           itermediaryLength = itermediaryLength + 1
           index = index + 1

    if(itermediaryLength > maxLength):
        maxLength = itermediaryLength

    return maxLength

if __name__ == "__main__":
    print (lengthOfLongestSubstring("dvdf"))
    print (lengthOfLongestSubstring("abcabcbb"))
    print (lengthOfLongestSubstring("bbbbb"))
    print (lengthOfLongestSubstring("pwwkew"))
    print (lengthOfLongestSubstring(""))
    print (lengthOfLongestSubstring(" "))
