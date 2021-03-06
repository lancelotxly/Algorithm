class Queue_Error(Exception):
    def Queue_Overflow(self):
        print('Queue overflow')
    def Queue_Undeflow(self):
        print('Queue underflow')
'''
Queue Dict: using this method will leave a empty space, because to verify the fullness of the queue
            we use this condition: q.head == q.tail+1, but at this time q.tail have no data to input, so it is a empty space
            to avoid this problem, we let the q.head = q.tail = 0 not '1', to make the length of Queue is 'n' 
'''
class Queue_Dict():
    def __init__(self,n):
        self.QueueLength = n
        self.head = 0
        self.tail = 0

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
        if self.head == self.tail + 1 or (self.head == 0 and self.tail == self.QueueLength):
            return True
        else:
            return  False

    def EnQueue(self,x):
        try:
            if self.isQueueFull():
                raise Queue_Error
            else:
                self[self.tail] = x
                if self.tail == self.QueueLength:
                    self.tail = 0
                else:
                    self.tail = self.tail + 1
        except Queue_Error as e:
            e.Queue_Overflow()

    def DeQueue(self):
        try:
            if self.isQueueEmpty():
                raise Queue_Error
            else:
                x = self[self.head]
                if self.head == self.QueueLength:
                    self.head = 0
                else:
                    self.head = self.head + 1
                return x
        except Queue_Error as e:
            e.Queue_Undeflow()

class Queue_List():
    def __init__(self,n):
        self.QueueLength = n
        self.head = 0
        self.tail = 0
        self.DataList = [0]*(n+1)

    def isQueueEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def isQueueFull(self):
        if self.head == self.tail + 1 or (self.head == 0 and self.tail == self.QueueLength):
            return True
        else:
            return False

    def EnQueue(self,x):
        try:
            if self.isQueueFull():
                raise  Queue_Error
            else:
                self.DataList[self.tail] = x
                if self.tail == self.QueueLength:
                    self.tail = 0
                else:
                    self.tail = self.tail + 1
        except Queue_Error as e:
            e.Queue_Overflow()

    def DeQueue(self):
        try:
            if self.isQueueEmpty():
                raise Queue_Error
            else:
                x = self.DataList[self.head]
                if self.head == self.QueueLength:
                    self.head = 0
                else:
                    self.head = self.head + 1
                return  x
        except Queue_Error as e:
            e.Queue_Undeflow()

class Double_End_Queue():
    def __init__(self,n):
        self.QueueLength = n
        self.head = 0
        self.tail = 0
        self.DataList = [0] * (n+2)

    def isQueueEmpty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def isQueueFull(self):
        if self.head == self.tail + 1 or (self.head == 0 and self.tail == self.QueueLength + 1):
            return True
        else:
            return False

    def Head_EnQueue(self,x):
        try:
            if self.isQueueFull():
                raise Queue_Error
            else:
                self.DataList[self.head] = x
                if self.head == 0:
                    self.head = self.QueueLength + 1
                else:
                    self.head = self.head - 1
        except Queue_Error as e:
            e.Queue_Overflow()

    def Head_DeQueue(self):
        try:
            if self.isQueueEmpty():
                raise Queue_Error
            else:
                if self.head == self.QueueLength + 1:
                    self.head = 0
                else:
                    self.head = self.head + 1
                x = self.DataList[self.head]
                return  x
        except Queue_Error as e:
            e.Queue_Undeflow()

    def Tail_EnQueue(self,x):
        try:
            if self.isQueueFull():
                raise Queue_Error
            else:
                self.DataList[self.tail] = x
                if self.tail == self.QueueLength + 1:
                    self.tail = 0
                else:
                    self.tail = self.tail - 1
        except Queue_Error as e:
            e.Queue_Overflow()

    def Tail_DeQueue(self):
        try:
            if self.isQueueEmpty():
                raise Queue_Error
            else:
                if self.tail == 0:
                    self.tail = self.QueueLength + 1
                else:
                    self.tail = self.tail -1
                x = self.DataList[self.tail]
                return x
        except Queue_Error as e:
            e.Queue_Undeflow()

class Queue_comesfrom_Stack():
    pass


