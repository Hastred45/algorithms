# ID - 72822623

OPERATIONS = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y,
              '*': lambda x, y: x * y,
              '/': lambda x, y: x // y, }


class EmptyError(Exception):
    pass


class PolandStack:
    def __init__(self) -> None:
        self.__items = []

    def is_empty(self) -> bool:
        '''Проверка на пустой стек'''
        if self.__items:
            return False
        else:
            return True

    def push(self, number: int) -> None:
        '''Помещает значение не вершину стека'''
        self.__items.append(number)

    def pop(self):
        '''Возвращает значение с вершины стека'''
        if self.is_empty():
            raise EmptyError
        return self.__items.pop()


def operations(num1: int, num2: int, operator: str) -> int:
    '''
    Принимает на вход два числа и оператор.
    Производит вычисления и возвращает результат.
    '''
    try:
        return OPERATIONS[operator](num1, num2)
    except KeyError:
        return 'неизвестная операция'


if __name__ == '__main__':
    data = input().split()
    stack = PolandStack()
    for elem in data:
        if elem not in OPERATIONS:
            elem = int(elem)
            stack.push(elem)
        else:
            try:
                num2 = stack.pop()
                num1 = stack.pop()
            except EmptyError:
                continue
            calc = operations(num1, num2, elem)
            stack.push(calc)
    print(stack.pop())
