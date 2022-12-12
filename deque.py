# ID - 72823856


class EmptyError(Exception):
    pass


class OverflowError(Exception):
    pass


class Deque:
    max_size: int

    def __init__(self, max_size: int) -> None:
        self.__elements = [None] * max_size
        self.__max_size = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self) -> bool:
        '''Проверка на пустую деку'''
        return self.__size == 0

    def push_back(self, value):
        '''Добавляет элемент в хвост и передвигает его'''
        if self.__size != self.__max_size:
            self.__elements[self.__tail] = value
            self.__tail = (self.__tail + 1) % self.__max_size
            self.__size += 1
        else:
            raise OverflowError

    def push_front(self, value):
        '''Добавляет элемент в голову и передвигает ее'''
        if self.__size != self.__max_size:
            self.__elements[self.__head - 1] = value
            self.__head = (self.__head - 1) % self.__max_size
            self.__size += 1
        else:
            raise OverflowError

    def pop_back(self):
        '''Удаляет элемент из хвоста и передвигает его'''
        if self.is_empty():
            raise EmptyError
        else:
            value = self.__elements[self.__tail - 1]
            self.__elements[self.__tail - 1] = None
            self.__tail = (self.__tail - 1) % self.__max_size
            self.__size -= 1
            return value

    def pop_front(self):
        '''Удаляет элемент из головы и передвигает ее'''
        if self.is_empty():
            raise EmptyError
        else:
            value = self.__elements[self.__head]
            self.__elements[self.__head] = None
            self.__head = (self.__head + 1) % self.__max_size
            self.__size -= 1
            return value


if __name__ == '__main__':
    num_of_oper = int(input())
    deque_size = int(input())
    deque = Deque(deque_size)
    result = []
    for _ in range(num_of_oper):
        data = input().split()
        if len(data) == 2:
            try:
                getattr(deque, data[0])(data[1])
            except OverflowError:
                result.append('error')
        else:
            try:
                result.append(getattr(deque, data[0])())
            except EmptyError:
                result.append('error')
    for answer in result:
        print(answer)
