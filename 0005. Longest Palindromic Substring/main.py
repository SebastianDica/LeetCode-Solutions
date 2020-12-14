def longestPalindrome(s: str) -> str:
    length = len(s)
    oddPalindromes = {}
    evenPalindromes = {}

    maxLength = 0
    maxPalindrome = ""

    # Odd palindrome case
    for i in range(0, length):
        oddPalindromes[i] = s[i]
        maxLength = 1
        maxPalindrome = oddPalindromes[i]

    # Even palindrome case
    for i in range(1, length):
        if s[i-1] == s[i]:
            evenPalindromes[i - 1] = s[i - 1] + s[i]
            maxLength = 2
            maxPalindrome = evenPalindromes[i - 1]

    # Expanded palindromes
    expand = 1
    while len(oddPalindromes) > 0 or len(evenPalindromes) > 0:
        for index in list(oddPalindromes):
            if (index - expand >= 0 and index + expand < length and s[index - expand] == s[index  + expand]):
                if (2 * expand + 1 > maxLength):
                    maxLength = 2 * expand + 1
                    maxPalindrome = s[index - expand:index + expand + 1]
            else:
                del oddPalindromes[index]

        for index in list(evenPalindromes):
            if (index - expand >= 0 and index + expand + 1 < length and s[index - expand] == s[index  + expand + 1]):
                if (2 * expand + 2 > maxLength):
                    maxLength = 2 * expand + 2
                    maxPalindrome = s[index - expand:index + expand + 2]
            else:
                del evenPalindromes[index]

        expand = expand + 1

    return maxPalindrome

if __name__ == "__main__":
    print (longestPalindrome("babad"), "expected bab or aba")
    print (longestPalindrome("cbbd"), "expected bb")
    print (longestPalindrome("cbbc"), "expected cbbc")
    print (longestPalindrome("a"), "expected a")
    print (longestPalindrome("ac"), "expected a")
    print (longestPalindrome("aca"), "expected aca")
    print (longestPalindrome("abcdeabcdedcba"), "expected abcdedcba")
    print (longestPalindrome("abcdedcb1abcdedcba"), "expected abcdedcba")
