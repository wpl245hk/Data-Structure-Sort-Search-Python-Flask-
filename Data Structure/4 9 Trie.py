class Trie():

    def __init__(self, root=None):
        self.dict = {}
        if root is None:
            ...
        elif type(root) is int:
            self.insert(root)
        else:
            for letter in root:
                self.insert(letter)

    def insert(self, words):
        curr = self.dict
        for i in range(len(words)):
            if words[i] not in curr.keys():
                curr[words[i]] = {}
            curr = curr[words[i]]
        curr['*'] = None 

    def delete(self, words):
        curr = self.dict
        for i in range(len(words)):
            if words[i] in curr.keys():
                curr = curr[words[i]]
            else:
                print("Invalid delete")
                return                

        if '*' in curr.keys():
            del curr['*']
        else:
            print("Invalid delete")

        def del_recursion(curr, words, j):
                # base case for delete completion
                if j == 0:
                    print("delete complete")
                    return
                
                # reach last position
                for i in range(j):
                    curr = curr[words[i]]

                # delete word only if last position has sole key
                if len(curr.keys()) == 1:
                    del curr[words[i]]
                    del_recursion(curr, words, i-1)
                # else, terminate deletion
                else:
                    print("delete complete")
                    return
 
        del_recursion(self.dict, words, len(words))

    def dfs(self, words):
        query = []
        curr = self.dict
        for i in range(len(words)):
            if words[i] in curr.keys():
                curr = curr[words[i]]
            else:
                print("Invalid query")
                return

        def recursion(curr, words):
            for k in curr.keys():
                if k == '*':
                    query.append(words)
                else:                   
                    recursion(curr[k], words + k)

        recursion(curr, words)
        return query

    def traverse(self):
        print(self.dict)

# test cases
#t = Trie(["when", "who"])
#t.insert("was")
#t.insert("word")
#t.insert("war")
#t.insert("what")
#t.insert("where")
#print(t.dfs("wh"))
# output: ['what', 'where']
#t.delete("what")
#print(t.dfs("wh"))
# output: ['what']
#t.traverse()

