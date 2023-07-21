import time
import random

random_numbers = []

for i in range (0, 1000):
    n = random.randint(0,1000)
    random_numbers.append(n)

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            str(node.v) + ' '
            self._printTree(node.r)

#     3
# 0     4
#   2      8
tree = Tree()
for i in range(len(random_numbers)):
    tree.add(random_numbers[i])

start_time = time.time()

for i in range(100):
    #tree.printTree()
    for j in range(len(random_numbers)):
        for x in range(len(random_numbers)):
            x+j

totaltime = time.time() - start_time
print(totaltime)