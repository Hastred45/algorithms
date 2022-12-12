class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
  
    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return 'OK'
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return 'None'
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return 'None'
        return self.queue[self.head]

    def q_size(self):
        return self.size

n = int(input())
k = int(input())
queue = Queue(k)
result = []
for i in range(n):
    action = input().split()
    if action[0] == 'push':
        a = queue.push(action[1])
        if a == 'error':
            result.append(a)
    if action[0] == 'pop':
        result.append(queue.pop())
    if action[0] == 'peek':
        result.append(queue.peek())
    if action[0] == 'size':
        result.append(queue.q_size())
        
for i in result:
    print(i)   