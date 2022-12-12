class StackMax:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, number):
        number = int(number)
        self.items.append(number)

    def pop(self):
        if self.isEmpty():
            return 'error'
        return self.items.pop()
    
    def get_max(self):
        if self.isEmpty():
            return 'None'
        return max(self.items)      


n = int(input())
stack = StackMax()
result = []
for i in range(n):
    action = input().split()
    if action[0] == 'push':
        stack.push(action[1])
    if action[0] == 'pop':
        if stack.pop() == 'error':
            result.append('error')
    if action[0] == 'get_max':
        result.append(stack.get_max())
        
for i in result:
    print(i)        
