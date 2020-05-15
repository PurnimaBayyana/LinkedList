class Node:

    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
     self.head = None

    def insert(self,value):

     self.head = Node(value,self.head)

    def includes(self,key):
        current = self.head
        while current:
         if current.value == key:
          return True

          current = current.next

    
         return False

    def tostring(self):
        stringValue = self.head
        tostring_value = ''
        while stringValue is not None:
            tostring_value = tostring_value + '{' + stringValue.value + '} -> '
            stringValue = stringValue.next
        tostring_value = tostring_value + 'NULL'
        return tostring_value   


