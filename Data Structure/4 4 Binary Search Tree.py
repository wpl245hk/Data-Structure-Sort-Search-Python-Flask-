from scripts.Wrapper import avg_10times

class BST_node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST():
    def __init__(self, root):
        if type(root) is int:
            self.root = BST_node(root)
        else:
            self.sort_time = self.sort(root)[1]

    def insertNodes(self, values):
        for value in values:
            self.insertNode(value)

    def insertNode(self, value):
        curr = self.root
        while curr:
            if value <= curr.value:
                if curr.left is None:
                    curr.left = BST_node(value)   
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = BST_node(value)
                    break
                curr = curr.right

    @avg_10times
    def sort(self, root):
        self.root = BST_node(root[0])
        self.insertNodes(root[1:])
        return        

    @avg_10times
    def search(self, data_item):
        curr = self.root
        while curr:
            if data_item == curr.value:
                return
            elif data_item < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        print("The element cannot be found.")
        return 0
    
    def inorder(self):
        if self.root is None:
            print("There is no item.")
        else:
            def traverse(curr):
                if curr is None:
                    return []
                return traverse(curr.left)+ [curr.value] +traverse(curr.right)

            print(traverse(self.root)) 
        


# test case
#a = BST(4)
#a.insertNode(8)
#a.insertNode(3)
#a.insertNode(1)
#a.insertNode(6)
#a.insertNode(0)
#a.insertNode(10)
#a.insertNode(14)
#a.insertNode(4)
#a.insertNode(-7)
#a.inorder()

#del a
#a = BST([4,8,3,1,6,0,10,14,4,-7])
#a.inorder()
