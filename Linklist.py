class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Link_Error(Exception):
    def Not_Found(self,data):
        print('%d not found' % data)

class Single_Link_List():
    def __init__(self):
        self.head = None
        self.temp = None
        self.Lenght = 0

    def Insert_Link_Tail(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.temp = node
        else:
            self.temp.next = node
            self.temp = node
        self.Lenght = self.Lenght + 1

    def Insert_Link_Head(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node


    def Search_Link(self,data):
        self.temp = self.head
        while self.temp != None and self.temp.data != data:
            self.temp = self.temp.next
        if self.temp != None:
            return self.temp.data
        else:
            return None

    def Delete_Link(self,data):
        temp1 = temp2 = self.head
        while temp1 != None and temp1.data != data:
            temp2 = temp1
            temp1 = temp1.next

        if temp1 != None:
          if temp2 != temp1:
              temp2.next = temp1.next
          else:
              self.head = temp1.next
        else:
            print('%d is not found' % data)

    def Print_Link(self):
        self.temp = self.head
        while self.temp != None:
            data = self.temp.data
            self.temp = self.temp.next
            print(data)


# test
L = Single_Link_List()
for i in range(1,6):
    L.Insert_Link_Head(i)
L.Print_Link()
print(L.Search_Link(0))
L.Delete_Link(3)
L.Print_Link()