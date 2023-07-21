import timeit

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insertHead(self, node):
        if self.head is None:
            self.head = Node(node)
        else:
            temp = self.head
            self.head = Node(node)
            self.head.next = temp

    def insertNext(self, prevNode, nextNode):
        temp = prevNode.next
        prevNode.next = Node(nextNode)
        prevNode.next.next = temp
        if prevNode == self.head:
            self.tail = prevNode.next

    def insertTail(self, node):
        if self.head is None:
            self.head = Node(node)
        elif self.tail is None:
            self.head.next = Node(node)
            self.tail = self.head.next
        else:
            self.tail.next = Node(node)
            self.tail = self.tail.next

    def swap(self, nodeOne, nodeTwo):
        prevOne = currOne = prevTwo = currTwo = None
        prev = curr =self.head
        while curr is not None:
            if curr.value == nodeOne:
                    prevOne = prev
                    currOne = curr
            elif curr.value == nodeTwo:
                    prevTwo = prev
                    currTwo = curr

            if currOne is not None and currTwo is not None:
                if self.head.value == nodeOne:
                    
                    currOne = prevTwo.next
                    currTwo.next, currOne.next = currOne.next, currTwo.next
                    self.head = currTwo
                elif self.head.value == nodeTwo:
                    
                    prevTwo = prevOne.next
                    currTwo.next, currOne.next = currOne.next, currTwo.next
                    self.head = currOne
                else:
                    prevTwo.next, prevOne.next = prevOne.next, prevTwo.next
                    currTwo.next, currOne.next = currOne.next, currTwo.next

                if self.tail.value == nodeOne:
                    self.tail = currTwo
                elif self.tail.value == nodeTwo:
                    self.tail = currOne
                
                return
            prev, curr = curr, curr.next
        
        print("The node cannot be found.")


    def deleteNode(self, node):        
        prev = curr = self.head
        while curr is not None:
            if curr.value == node:
                if curr == self.head:
                    self.head = curr.next
                elif curr == self.tail:
                    self.tail = prev
                    prev.next = None
                else:
                    prev.next = curr.next
                return
            prev, curr = curr, curr.next
            
        print("The node cannot be found.")

    def traverse(self):
        print('linked list:', self.head.value, end="")
        curr = self.head
        while curr.next is not None:
            print("->", curr.next.value, end = "")
            curr = curr.next

    # count search time
    def searchNodeTime(self, node):
        starttime = timeit.default_timer()

        curr = self.head
        while curr is not None:
            if curr.value == node:
                # search successful
                return timeit.default_timer() - starttime
            curr = curr.next
            
        # search unsuccessful
        print("The node cannot be found.")
        return 0
        


