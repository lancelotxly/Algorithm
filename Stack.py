'''
We build a stack base on three data-structure: 1) Stack_Dict(n) # we save the data into the class internal dict i.e '__dict__'
                                               2) Stack_list(n) # we define a new 'data_list' at the internal of the class
                                               3) Stack_Link(n) # we build node-link to save the data
All Stacks have 4 methods: isStackEmpty(), isStackFull(), push(data), pop()
, one attribution； stack.top
, and two errors: Stack_Overflow()  # push(data) when stack.top == stack.length
                  Stack_Underflow() # pop(data) when stack.top == 0
'''
'''
Stack error : 1) Stack_overflow  # Stack is fulled, then push data into the stack is error
              2) Stack_underflow # Stack is empty, then pop data from the stack is error
'''
class Stack_error(Exception):
    def Stack_Overflow(self):
        print('error: Stack overflow')

    def Stack_Underflow(self):
        print('error: Stack underflow')

'''
Stack based on Dict: we save the data of the stack into the class internal __dict__
                     then the arrange of the data is from '1' to 'n'
'''
class Stack_Dict():
   def __init__(self,n):
       self.stacklength = n
       self.top = 0

   def __setitem__(self, key, value):
       self.__dict__[key] = value

   def __getitem__(self, item):
       return self.__dict__[item]

   def isStackEmpty(self):
       if self.top == 0:
           return True
       else:
           return False

   def isStackFull(self):
       if self.top == self.stacklength:
           return True
       else:
           return False

   def push(self,x):
       try:
           if self.isStackFull():
               raise Stack_error
           else:
               self.top = self.top + 1
               self[self.top] = x
       except Stack_error as e:
           e.Stack_Overflow()

   def pop(self):
       try:
           if self.isStackEmpty():
               raise Stack_error
           else:
               self.top = self.top - 1
               return self[self.top+1]
       except Stack_error as e:
           e.Stack_Underflow()

   def clearStack(self):
        self.top = 0

'''
Stack based on List: we introduce a new list at the internal of the class to save the data
                     then the arrange of the data is from '0' to 'n-1'
'''
class Stack_List():
      def __init__(self,n):
          self.stacklength = n
          self.Datalist = []
          self.top = 0

      def isStackEmpty(self):
          if self.top == 0:
              return True
          else:
              return False

      def isStackFull(self):
          if self.top == self.stacklength:
              return True
          else:
              return False

      def push(self,x):
          try:
              if self.isStackFull():
                  raise Stack_error
              else:
                  self.top = self.top + 1
                  self.Datalist.append(x)
          except Stack_error as e:
              e.Stack_Overflow()

      def pop(self):
          try:
              if self.isStackEmpty():
                  raise Stack_error
              else:
                  self.top = self.top - 1
                  return self.Datalist[self.top] # here, we don't need to push '1' on self.top,
                                                 # because the data is saved in a list which arrange is from '0' to 'n-1'
          except Stack_error as e:
              e.Stack_Underflow()

class Stack_Link():
    pass

'''
Stack twins: we build the twins stacks in the main stack (with stack.length = n), i.e L_stack and R_stack
             which includes: 1) isStackEmpty()  # Left_top == 0 and Right_top == stack.length + 1
                             2) isStackFull()   # Left_top + 1 == Right_top or Right_Top - 1 == Left_top
                             3) push('Left/Right',x)  # if isStackFull() == True, then push will overflow error
                             4) pop('Left/Right')  # if 'Left' and Left_top == 0, then pop will underflow
                                                     if 'Right' and Right_top == n + 1, then pop will underflow too.
'''
class Stack_Twins():
    def __init__(self,n):
        self.stacklength = n
        self.Left_top = 0
        self.Right_top = n + 1


    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def isStackEmpty(self):
        if self.Left_top == 0 and self.Right_top == self.stacklength + 1:
            return True
        else:
            return False

    def isStackFull(self):
        if self.Left_top + 1 == self.Right_top or self.Right_top - 1 == self.Left_top:
            return True
        else:
            return False

    def push(self,label,x):
       try:
           if self.isStackFull():
               raise Stack_error
           elif label == 'Left':
               self.Left_top = self.Left_top + 1
               self[self.Left_top] = x
           elif label == 'Right':
               self.Right_top = self.Right_top - 1
               self[self.Right_top] = x
       except Stack_error as e:
           e.Stack_Overflow()

    def pop(self,label):
        if label == 'Left':
            try:
                if self.Left_top == 0:
                    raise Stack_error
                else:
                    self.Left_top = self.Left_top - 1
                    return self[self.Left_top+1]
            except Stack_error as e:
                e.Stack_Underflow()
        if label == 'Right':
            try:
                if self.Right_top == self.stacklength + 1:
                    raise Stack_error
                else:
                    self.Right_top = self.Right_top + 1
                    return self[self.Right_top-1]
            except Stack_error as e:
                e.Stack_Underflow()

s= Stack_Twins(5)
s.push('Left',1)
s.push('Right',5)
s.push('Left',2)
s.push('Right',4)
s.push('Left',3)
print(s.pop('Right'))
print(s.pop('Right'))
print(s.pop('Right'))
print(s.__dict__)

class Stack_comesfrom_Queue():
    pass