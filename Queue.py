class Queue_Error(Exception):
    def Queue_Overflow(self):
        print('Queue overflow')
    def Queue_Undeflow(self):
        print('Queue underflow')

class Queue_Dict():
    def __init__(self,n):
        self.queuelength = n
        self.head = 1
        self.tail = 1

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def isQueueEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def isQueueFull(self):
        if self.head == self.tail + 1:
            return True
        else:
            return False

