class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        '''Return the root node.'''
        return self.root

    def add_node(self, item):
        '''Insert an element into the bst.'''
        if self.root is None:
            self.root = Node(item)
        else:
            nd = self.root
            while nd is not None:
                if item < nd.data:
                    if nd.left is None:
                        nd.left = Node(item)
                        return
                    else:
                        nd = nd.left
                else:
                    if nd.right is None:
                        nd.right = Node(item)
                        return
                    else:
                        nd = nd.right


    def remove(self, item):
        # empty tree
        if self.root is None:
            return 0
            
        # item is in root node  
        elif self.root.data == item:
            if self.root.left is None and self.root.rightChild is None:
                self.root = None
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
            elif self.root.left and self.root.right:
                delNodeParent = self.root
                delNode = self.root.right
                while delNode.left:
                    delNodeParent = delNode
                    delNode = delNode.left
                    
                self.root.data = delNode.data
                if delNode.right:
                    if delNodeParent.data > delNode.data:
                        delNodeParent.left = delNode.right
                    elif delNodeParent.data < delNode.data:
                        delNodeParent.right = delNode.right
                else:
                    if delNode.data < delNodeParent.data:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None
                        
            return 1
        
        parent = None
        node = self.root
        
        # find node to remove
        while node and node.data != item:
            parent = node
            if item < node.data:
                node = node.left
            elif item > node.data:
                node = node.right
        
        # case 1: item not found
        if node is None or node.data != item:
            return 0
            
        # case 2: remove-node has no children
        elif node.left is None and node.right is None:
            if item < parent.data:
                parent.left = None
            else:
                parent.right = None
            return 1
            
        # case 3: remove-node has left child only
        elif node.left and node.right is None:
            if item < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return 1
            
        # case 4: remove-node has right child only
        elif node.left is None and node.right:
            if item < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            return 1
            
        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left
                
            node.data = delNode.data
            if delNode.right:
                if delNodeParent.data > delNode.data:
                    delNodeParent.left = delNode.right
                elif delNodeParent.data < delNode.data:
                    delNodeParent.right = delNode.right
            else:
                if delNode.data < delNodeParent.data:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None

    def search(self, item):
        '''Iteratively search an element.'''
        if self.root is None:
            return 0
        else:
            nd = self.root
            while nd is not None:
                if nd.data == item:
                    return 1
                elif nd.data < item:
                    nd = nd.right
                else:
                    nd = nd.left
            return 0

    

with open("binary-search-tree-in.txt", "r+") as TextFile:
    fo = open("binary-search-tree-out.txr", "w")
    content = TextFile.readlines()
    content = [x.strip() for x in content]
    t=BinarySearchTree()
    i=0
    newcontent = map(int, content)
    while True:
        if(newcontent[i]==1):
            t.add_node(newcontent[i+1])
            i+=2
        elif(newcontent[i]==0):
            x=t.remove(i+1)
            print(str(x))
            i+=2
        elif(newcontent[i]==2):
            a=t.search(newcontent[i+1])
            print(str(a))
            i+=2
        elif(content[i]!='-1'):
            fo.close()
            TextFile.close()
            break

