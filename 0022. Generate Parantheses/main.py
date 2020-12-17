from typing import List

def generateParenthesis(n: int) -> List[str]:
    return generateParanthesisQuota(0, 0, n, [""])

def generateParanthesisQuota(openQuota: int, closedQuota: int, maxQuota: int, generated: List[str]) -> List[str]:
    if openQuota == closedQuota == maxQuota:
        return generated
        
    openList = []
    closeList = []

    if openQuota < maxQuota:
        if closedQuota < openQuota:
            openList = generateParanthesisQuota(openQuota + 1, closedQuota , maxQuota, [elem + "(" for elem in generated])
            closeList = generateParanthesisQuota(openQuota, closedQuota + 1 , maxQuota, [elem + ")" for elem in generated])
        else:
            openList = generateParanthesisQuota(openQuota + 1, closedQuota , maxQuota, [elem + "(" for elem in generated])
    elif closedQuota < openQuota:
        closeList = generateParanthesisQuota(openQuota, closedQuota + 1 , maxQuota, [elem + ")" for elem in generated])

    return openList + closeList

if __name__ == '__main__':
    print (generateParenthesis(1), "expected ['()']")
    print (generateParenthesis(2), "expected ['(())','()()']")
    print (generateParenthesis(3), "expected ['((()))','(()())','(())()','()(())','()()()']")
    print (generateParenthesis(4), "expected ['(((())))','((()()))','((())())','((()))()','(()(()))','(()()())','(()())()','(())(())','(())()()','()((()))','()(()())','()(())()','()()(())','()()()()']")
