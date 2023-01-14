class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:  # check if the value exist
            return  # if the value exist simply return

        if data < self.data:  # allow to add the data in the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:  # used for searching
            return True

        if val < self.data:  # the value might be in left subtree
            if self.left:  # checking if the value is actually at left subtree
                return self.left.search(val)  # it will do recursion
            else:
                return False

        if val > self.data:  # the value might be in the right subtree
            if self.right:  # checking if the value is actually at right subtree
                return self.right.search(val)  # it will do recursion
            else:
                return False

