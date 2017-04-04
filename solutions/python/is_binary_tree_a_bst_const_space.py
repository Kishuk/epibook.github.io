from binary_tree_prototype import BinaryTreeNode


# @include
def is_binary_tree_bst(root):
    n = root
    # Stores the value of previous visited node.
    prev_value = float('-inf')
    result = True

    while n:
        if n.left:
            # Finds the predecessor of n.
            pre = n.left
            while pre.right and pre.right is not n:
                pre = pre.right

            # Processes the successor link.
            if pre.right:  # pre.right is n.
                # Reverts the successor link if predecessor's successor is n.
                pre.right = None
                if prev_value > n.data:
                    result = False
                prev_value = n.data
                n = n.right
            else:  # If predecessor's successor is not n.
                pre.right = n
                n = n.left
        else:
            if prev_value > n.data:
                result = False
            prev_value = n.data
            n = n.right
    return result


# @exclude


def main():
    #      3
    #    2   5
    #  1    4 6
    tree = BinaryTreeNode(3)
    tree.left = BinaryTreeNode(2)
    tree.left.left = BinaryTreeNode(1)
    tree.right = BinaryTreeNode(5)
    tree.right.left = BinaryTreeNode(4)
    tree.right.right = BinaryTreeNode(6)
    # should output True.
    assert is_binary_tree_bst(tree)
    print(is_binary_tree_bst(tree))
    #      10
    #    2   5
    #  1    4 6
    tree.data = 10
    # should output False.
    assert not is_binary_tree_bst(tree)
    print(is_binary_tree_bst(tree))
    # should output True.
    assert is_binary_tree_bst(None)
    print(is_binary_tree_bst(None))


if __name__ == '__main__':
    main()
