class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not len(self.items) > 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackException("Cannot pop on an empty stack!")
        last_item = self.items[-1]
        del self.items[-1]
        return last_item

    def peek(self):
        last_item = self.items[-1]
        return last_item


class EmptyStackException(Exception):
    pass
