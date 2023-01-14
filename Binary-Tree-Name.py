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

    def in_order_traversal(self):
        elements = []  # to fill the elements in the binary
        if self.left:  # visit the left tree
            elements += self.left.in_order_traversal()

        elements.append(self.data)  # visit the base node

        if self.right:  # visit the right tree
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def find_max(self):  # finding maximum element which is in the right
        if self.right is None:  # setting if there's no element in the right then it is the maximum
            return self.data
        return self.right.find_max()

    def find_min(self):  # finding minimum element which is in the left
        if self.left is None:  # setting if there's no element in the left then it is the minimum
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:  # finding the value if the value is less than the data
            if self.left:
                self.left = self.left.delete(val)  # record the deleted value
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:  # if the element doesn't exist and return none
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

