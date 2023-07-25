from scripts.Wrapper import avg_10times


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
            # swap continue
            if curr.value == nodeOne:
                    prevOne = prev
                    currOne = curr
            elif curr.value == nodeTwo:
                    prevTwo = prev
                    currTwo = curr

            # swap complete
            if currOne is not None and currTwo is not None:
                
                # self.head is one of the nodes
                if self.head.value == nodeOne:           
                    prevTwo.next = currOne
                    currTwo.next, currOne.next = currOne.next, currTwo.next
                    self.head = currTwo
                elif self.head.value == nodeTwo:
                    prevOne.next = currTwo
                    currTwo.next, currOne.next = currOne.next, currTwo.next
                    self.head = currOne

                # self.head and self.tail are not one of the nodes
                else:
                    prevTwo.next, prevOne.next = prevOne.next, prevTwo.next
                    currTwo.next, currOne.next = currOne.next, currTwo.next

                # self.tail is one of the nodes
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

    # for each iteration, swap largest element to last comparation position
    @avg_10times
    def bubbleSort(self):
        def iteration(count_end=0,first_trial=True):
            # last iteration compare position 0 with position 0, hence no need
            if count_end == 1:
                return
            
            prev = curr =self.head
            if first_trial:
                
                while curr.next is not None:
                    if curr.value > curr.next.value:
                        # self.head is one of the nodes
                        if curr == self.head:   
                            self.head = curr.next      
                            curr.next = curr.next.next  
                            self.head.next = curr
                            
                        else:
                            # self.tail is one of the nodes
                            if curr.next == self.tail:  
                                self.tail = curr
                            prev.next = curr.next
                            curr.next = curr.next.next
                            prev.next.next = curr
                        prev = prev.next
                    else:
                        prev, curr = curr, curr.next
                    # In first_trail, calculate the count_end
                    count_end += 1

            else:
                count_now = count_end
                while count_now > 0 :
                    if curr.value > curr.next.value:
                        # self.head is one of the nodes
                        if curr == self.head:   
                            self.head = curr.next      
                            curr.next = curr.next.next  
                            self.head.next = curr
                            
                        else:
                            prev.next = curr.next
                            curr.next = curr.next.next
                            prev.next.next = curr
                        prev = prev.next
                    else:
                        prev, curr = curr, curr.next
                    # utilize the count_end in first_trail
                    count_now -= 1

            # last comparation position decreae by 1
            iteration(count_end-1, False)

        iteration()
        return


    @avg_10times
    def searchNodeTime(self, node):

        curr = self.head
        while curr is not None:
            if curr.value == node:
                # search successful
                return
            curr = curr.next
            
        # search unsuccessful
        print("The node cannot be found.")
        return 0
        
    def traverse(self):
        print('linked list:', self.head.value, end="")
        curr = self.head
        while curr.next is not None:
            print("->", curr.next.value, end = "")
            curr = curr.next
        print()

# Test case
#llist = LinkedList()
#llist.insertHead(2)
#llist.insertTail(1)
#llist.insertHead(3)
#llist.insertTail(4)
#llist.insertNext(llist.head.next, 5)
#llist.traverse()

#print("\nAfter deleting an element:")
#llist.deleteNode(7)
#llist.traverse()

#print("\nAfter swapping elements:")
#llist.swap(4,3)
#llist.traverse()