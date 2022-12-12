def letterCombinations(digits):

    letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def backtrack(digits, path, res):
        if digits == '':
            res.append(path)
            return
        for letter in letters[digits[0]]:
            path += letter
            print(path)
            backtrack(digits[1:], path, res)
            path = path[:-1]
    res = []
    backtrack(digits, '', res)
    for x in res:
        print(x, end=' ')


vvod = '23'
letterCombinations(vvod)
