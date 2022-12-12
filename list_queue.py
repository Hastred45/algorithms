class ListQueue:
    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return self.value

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def get(self):
        if self.is_empty():
            return 'error'
        if self.size == 1:
            x = self.head
            self.head = self.Node()
            self.tail = self.Node()
            self.size -= 1
            return x
        if self.size == 2:
            x = self.head
            self.head = self.tail
            self.size -= 1
            return x
        x = self.head
        self.head = self.tail.next.next
        self.tail.next = self.head
        self.size -= 1
        return x

    def put(self, x):
        if self.size == 0:
            self.head = self.Node(value=x)
            self.tail = self.head
        else:
            self.tail.next = self.Node(value=x)
            self.tail.next.next = self.head
            self.tail = self.tail.next
        self.size += 1

    def __str__(self):
        return self.value


n = int(input())
s = ListQueue()
res = []
for i in range(n):
    command = input().split()
    if len(command) == 2:
        a = s.put(command[1])
        if a == 'error':
            res.append(a)
    if command[0] == 'get':
        res.append(s.get())
    if command[0] == 'size':
        res.append(s.size)

for x in res:
    print(x)
