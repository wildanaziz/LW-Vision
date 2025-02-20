class Node:
    def __init__(self, data, nextNode=None, prevNode=None):
        self.dataNode = data
        self.nextNode = nextNode
        self.prevNode = prevNode

class DoubleLL:
    def __init__(self, root=None):
        self.root = root
        self.last = root
        self.size = 0  

    def addNode(self, data):
        newNode = Node(data)

        if self.root is None:
            self.root = newNode
            self.last = newNode
        else:

            self.last.nextNode = newNode
            newNode.prevNode = self.last
            self.last = newNode
        
        self.size += 1  

    def findNode(self, data):
        currentNodeDLL = self.root  

        while currentNodeDLL is not None:
            if currentNodeDLL.dataNode == data:  
                return currentNodeDLL 
            currentNodeDLL = currentNodeDLL.nextNode  

        return None  

    def removeNodeDLL(self, data):
        currentNode = self.root

        while currentNode is not None:
            if currentNode.dataNode == data:
                # Jika node yang dihapus adalah root (node pertama)
                if currentNode == self.root:
                    self.root = currentNode.nextNode
                    if self.root:  # Jika masih ada node setelahnya
                        self.root.prevNode = None
                    else:
                        self.last = None  # Jika list menjadi kosong
                    
                # Jika node yang dihapus adalah node terakhir
                elif currentNode == self.last:
                    self.last = currentNode.prevNode
                    self.last.nextNode = None
                
                # Jika node di tengah
                else:
                    currentNode.prevNode.nextNode = currentNode.nextNode
                    currentNode.nextNode.prevNode = currentNode.prevNode
                
                self.size -= 1  # Kurangi ukuran list
                return "Data was successfully removed"

            currentNode = currentNode.nextNode

        return "Data was not found"

    def printListNode(self):
        currentNode = self.root
        
        while currentNode is not None:
            print(currentNode.dataNode, end=" <-> ")
            currentNode = currentNode.nextNode
            
        print("None")

doubleLL = DoubleLL()
doubleLL.addNode(2)
doubleLL.addNode(3)
doubleLL.addNode(4)
doubleLL.printListNode()
doubleLL.removeNodeDLL(3)
doubleLL.printListNode()