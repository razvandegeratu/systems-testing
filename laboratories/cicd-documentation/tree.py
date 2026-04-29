from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None
    


    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        pass


# Unit tests pentru functia find
def test_find_existing_data():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.find(3).data == 3, "Test failed: existing data not found"


def test_find_non_existing_data():
    tree = Tree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    assert tree.find(10) is None, "Test failed: non-existing data should return None"


def test_find_empty_tree():
    tree = Tree()
    assert tree.find(5) is None, "Test failed: finding data in an empty tree should return None"


