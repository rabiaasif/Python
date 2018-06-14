class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        self.stack = self.stack[1:]
    def push(self, number):
        self.stack.reverse()
        self.stack.append(number)
        self.stack.reverse()
    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False
    def display(self):
        for i in self.stack:
            print str(i) 
