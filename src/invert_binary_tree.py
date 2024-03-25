class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(tree) -> BinaryTree:
    if tree is not None and tree.left is not None and tree.right is not None:
        tree.left.value, tree.right.value = tree.right.value, tree.left.value
        invert_binary_tree(tree.left)
        invert_binary_tree(tree.right)
        return tree
