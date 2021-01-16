'''
Queue is a FIFO data structure -- first-in, first-out.
Deque is a double-ended queue, but we can use it for our queue.
We use append() to enqueue an item, and popleft() to dequeue an item.
'''
from collections import deque
class Queue():
    def __init__(self):
        self.queue = deque()
        self.size = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.queue.popleft()
        else: 
            return None

    def peek(self):
        if self.size > 0:
            ret_val = self.queue.popleft()
            self.queue.appendleft(ret_val)
            return ret_val
        else:
            return None

    def get_size(self):
        return self.size


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(1)
    queue.enqueue(-1)
    print('Size: ', queue.get_size())
    print(queue.dequeue())
    print(queue.peek())
    print('Size: ', queue.get_size())