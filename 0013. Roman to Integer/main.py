import math

def romanToInt(s: str) -> int:
    endInteger = 0

    # Hmm, feel like this could be more generic
    transitionMap = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,

        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    index = 0

    while index < len(s):
        processed = False
        if(index + 1 < len(s)):
            if s[index] + s[index+1] in transitionMap:
                endInteger = endInteger + transitionMap[s[index] + s[index+1]]
                index = index + 1 # to skip the secondary processed roman numeral
                processed = True
        if not processed:
            endInteger = endInteger + transitionMap[s[index]]
        index = index + 1

    return endInteger


if __name__ == "__main__":
    print (romanToInt("III"), "expected 3")
    print (romanToInt("X"), "expected 10")
    print (romanToInt("XX"), "expected 20")
    print (romanToInt("C"), "expected 100")
    print (romanToInt("CDI"), "expected 401")
    print (romanToInt("XII"), "expected 12")
    print (romanToInt("XI"), "expected 11")
    print (romanToInt("IV"), "expected 4")
    print (romanToInt("IX"), "expected 9")
    print (romanToInt("LVIII"), "expected 58")
    print (romanToInt("MCMXCIV"), "expected 1994")
