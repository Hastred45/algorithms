def check_brackets(sequence):
    '''
    Проверяет скобки на закрытость. Сначала заполняем стек
    открывающими скобками, а потом по словарю сравниваем с закрывающими.
    '''
    stack = []
    brackets = {']': '[', ')': '(', '}': '{'}  # Расширяем словарь если нужно

    for char in sequence:
        if char in brackets:
            top_element = stack.pop() if stack else '#'
            if brackets[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack


print(check_brackets('[({()})]'))  # True
print(check_brackets('[({)}]'))  # False
