from typing import List

def letterCombinations(digits: str) -> List[str]:
    if digits == "":
        return []

    letters = []

    letterMap = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    newLetters = letterMap[digits[0]]
    substring = digits[1:len(digits)]
    recursedLettersList = letterCombinations(substring)

    if recursedLettersList != []:
        for newLetter in newLetters:
            for recursedLetters in recursedLettersList:
                letters.append(newLetter + recursedLetters)
    else:
        letters = newLetters

    return letters

if __name__ == "__main__":
    print (letterCombinations("23"), "expected ['ad','ae','af','bd','be','bf','cd','ce','cf']")
    print (letterCombinations("22"), "expected ['aa','ab','ac','ba','bb','bc','ca','cb','cc']")
    print (letterCombinations(""), "expected []")
    print (letterCombinations("2"), "expected ['a', 'b', 'c']")
