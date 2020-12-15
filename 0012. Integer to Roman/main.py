import math

def intToRoman(num: int) -> str:
    endRoman = ""

    ones = "I"
    fives = "V"
    tens = "X"

    transitionMap = {
        # tens
        "I": "X",
        "X": "C",
        "C": "M",
        "M": "M",
        # fives
        "V": "L",
        "L": "D",
        "D": "D",
    }

    while num > 0:
        remainder = num % 10
        num = math.floor(num / 10)

        if remainder == 0:
            pass
        elif remainder > 0 and remainder < 4:
            endRoman = remainder * ones + endRoman
        elif remainder == 4:
            endRoman = ones + fives + endRoman
        elif remainder > 4 and remainder < 9:
            endRoman = fives + (remainder - 5) * ones + endRoman
        elif remainder == 9:
            endRoman = ones + tens + endRoman

        ones = transitionMap[ones]
        fives = transitionMap[fives]
        tens = transitionMap[tens]

    return endRoman


if __name__ == "__main__":
    print (intToRoman(3), "expected III")
    print (intToRoman(10), "expected X")
    print (intToRoman(20), "expected XX")
    print (intToRoman(100), "expected C")
    print (intToRoman(401), "expected CDI")
    print (intToRoman(12), "expected XII")
    print (intToRoman(11), "expected XI")
    print (intToRoman(4), "expected IV")
    print (intToRoman(9), "expected IX")
    print (intToRoman(58), "expected LVIII")
    print (intToRoman(1994), "expected MCMXCIV")
