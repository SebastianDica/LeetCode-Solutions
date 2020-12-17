from typing import List

def generateParenthesis(n: int) -> List[str]:
    if n == 0:
        return []

    if n == 1:
        return ['()']

    combos = set()

    lowerParantheses = generateParenthesis(n - 1)

    for parantheses in lowerParantheses:
        combos.add('(' + parantheses + ')')
        combos.add('()' + parantheses)
        combos.add(parantheses + '()')

    return list(combos)

if __name__ == '__main__':
    print (generateParenthesis(1), "expected ['()']")
    print (generateParenthesis(2), "expected ['(())','()()']")
    print (generateParenthesis(3), "expected ['((()))','(()())','(())()','()(())','()()()']")
    print (generateParenthesis(4), "expected ['(((())))','((()()))','((())())','((()))()','(()(()))','(()()())','(()())()','(())(())','(())()()','()((()))','()(()())','()(())()','()()(())','()()()()']")
