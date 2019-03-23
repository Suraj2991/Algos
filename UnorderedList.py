class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def setData(self, d):
        self.data = d
    
    def setNext(self, n):
        self.next = n
    
    def getData(self):
        return self.data
    def getNext(self):
        return self.next

class UnorderedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        curr = self.head
        count = 0
        while curr != None:
            curr = curr.getNext()
            count = count +1
        return count
    
    def search(self, item):
        found = False
        curr = self.head
        while curr != None and not found:
            if curr.getData() == item:
                found = True
            else:
                curr = curr.getNext()
        return found
    
    def remove(self, item):
        found = False
        curr = self.head
        prev = None
        while curr != None and not found:
            if curr.getData() == item:
                found = True
            else:
                prev = curr
                curr = curr.getNext()
        if prev == None:
            self.head = curr.getNext()
        else:
            prev.setNext(curr.getNext())
    
    def append(self, item):
        curr = self.head
        temp = Node(item)
        while curr.getNext() != None:
            curr = curr.getNext()
        curr.setNext(temp)
    
    def insert(self, item, pos):
        
        if self.size() >= pos:
            curr = self.head
            prev = None
            i = 1
            temp = Node(item)
            while i < pos:
                if curr.getNext() != None:
                    i = i+1
                    prev = curr
                    curr = curr.getNext()
            temp.setNext(curr)
            if prev == None:
                self.head = temp
            else:
                prev.setNext(temp)
        else:
            self.append(item)

def printList(L):

    curr = L.head
    while curr.getNext() != None:
        print(curr.getData())
        curr = curr.getNext()
    print(curr.getData())

x = UnorderedList()
x.add(12)
x.add(13)
x.add(17)
x.add(11)
x.search(11)
x.add(33)
printList(L)
x.remove(33)
printList(L)
x.append(3)
x.append(20)
x.add(33)
printList(L)
x.insert(40,5)
printList(L)
x.insert(32,2)
printList(L)

