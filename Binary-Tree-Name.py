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


def build_tree(elements):  # helps to take the elements
    root = BinarySearchTreeNode(elements[0])  # set the first element as a root node

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    name = ["U", "R", "I", "E", "L", "J",
            "E", "S", "M", "E", "R", "A", "L", "D", "A"]
    numbers = [17, 4, 1, 20, 12, 7, 9, 27, 18, 23, 8, 7, 32]
    name_tree = build_tree(name)
    numbers_tree = build_tree(numbers)
    print("-"*60)
    print(" "*20 + "BINARY TREE OF MY NAME")
    print("-" * 60)
    print("My Name: ", name)
    print("The Ascending order of My Name: ", name_tree.in_order_traversal())
    print("U is in the list? ----->", name_tree.search("U"))
    print("B is in the list? ----->", name_tree.search("B"))
    print("E is in the list? ----->", name_tree.search("E"))
    print("The Current Minimum value is :", name_tree.find_min())
    print("The Current Maximum value is:", name_tree.find_max())
    print("Pre order traversal of the list:", name_tree.pre_order_traversal())
    print("Post order traversal of the list:", name_tree.post_order_traversal())
    name_tree.delete("A")
    print("After deleting letter A. The Updated List are: ", name_tree.in_order_traversal())
    name_tree.delete("R")
    print("After deleting letter R. The Updated List are: ", name_tree.in_order_traversal())
    print("After deleting a Letter, the Minimum value is now :", name_tree.find_min())
    print("After deleting a Letter, the Maximum value is now :", name_tree.find_max())
    print("-" * 60)
    print(" " * 15 + "BINARY TREE OF MY CHOSEN NUMBER")
    print("-" * 60)
    print("My Chosen Number: ", numbers)
    print("The Ascending order of My Chosen Number: ", numbers_tree.in_order_traversal())
    print("20 is in the list? ----->", numbers_tree.search(20))
    print("25 is in the list? ----->", numbers_tree.search(25))
    print("13 is in the list? ----->", numbers_tree.search(13))
    print("The Current Minimum value is :", numbers_tree.find_min())
    print("The Current Maximum value is:", numbers_tree.find_max())
    print("Pre order traversal of the list:", numbers_tree.pre_order_traversal())
    print("Post order traversal of the list:", numbers_tree.post_order_traversal())
    numbers_tree.delete(32)
    print("After deleting Number 32. The Updated List are: ", numbers_tree.in_order_traversal())
    numbers_tree.delete(1)
    print("After deleting Number 1. The Updated List are: ", numbers_tree.in_order_traversal())
    print("After deleting a Number, the Minimum value is now : ", numbers_tree.find_min())
    print("After deleting a Number, the Maximum value is now : ", numbers_tree.find_max())
