class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(key=lambda x: x[0])

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)[1]
        return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0][1]
        return None

    def size(self):
        return len(self.queue)
