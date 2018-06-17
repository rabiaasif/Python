class Queue:
    def __init__(self):
        self.queue = []
    def pop(self):
        self.queue = self.queue[1:]
    def push(self, number):
        self.queue.append(number)
    def is_empty(self):
        if self.queue == []:
            return True
        else:
            return False
    def display(self):
        for i in self.queue:
            print str(i) 

                
