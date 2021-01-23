'''
Stack is a LIFO data structure -- last-in, first-out.
Use append() to push an item onto the stack.
Use pop() to remove an item.
'''
class Stack():
    def __init__(self):
        self.stack = list()
        self.size = 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if len(self.stack) > 0:
            self.size -= 1
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[self.size-1]
        else:
            return None

    def min(self):
        return min(self.stack)

    def __str__(self):
        return str(self.stack)

if __name__ == '__main__':
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(3)
    my_stack.push(4)
    my_stack.push(-1)
    print(my_stack)
    print('Min:', my_stack.min())
    print(my_stack.pop())
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.pop())
    print('Size:', my_stack.size)