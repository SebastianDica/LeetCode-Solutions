def convert(s: str, numRows: int) -> str:
    selectedRow = 0
    result = ""

    coreJump = numRows * 2 - 2
    if (coreJump == 0):
        coreJump = 1

    while(selectedRow < numRows):
        jump1 = coreJump - selectedRow * 2
        jump2 = coreJump - jump1

        jumped1 = False

        if (jump1 == 0 and jump2 != 0):
            jump1 = jump2
        elif (jump1 != 0 and jump2 == 0):
            jump2 = jump1

        selectedIndex = selectedRow
        while selectedIndex < len(s):
            result = result + s[selectedIndex]
            if(jumped1):
                selectedIndex = selectedIndex + jump2
                jumped1 = False
            else:
                selectedIndex = selectedIndex + jump1
                jumped1 = True

        selectedRow = selectedRow + 1

    return result

if __name__ == "__main__":
    print (convert("PAYPALISHIRING", 3), "expected PAHNAPLSIIGYIR")
    print (convert("PAYPALISHIRING", 4), "expected PINALSIGYAHRPI")
    print (convert("A", 1), "expected A")
    print (convert("PAYPALISHIRING", 1), "expected PAYPALISHIRING")
    print (convert("PAYPALISHIRING", 5), "expected PHASIYIRPLIGAN")

# 3
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# 4
#
# 1 6 6 P     I    N
# 2 4 2 A   L S  I G
# 3 2 4 Y A   H R
# 4 6 6 P     I
#
# 5
#
# P     H
# A   S I
# Y  I  R
# P L   I G
# A     N
