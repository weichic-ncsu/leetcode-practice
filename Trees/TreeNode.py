# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_left_child_idx(idx):
    return idx*2 + 1
def get_right_child_idx(idx):
    return idx*2 + 2

def print_tree_node(root):
    if root:
        print("root: ", root.val)
    else:
        print("None")
        return

    if root.left:
        print("left child: ", root.left.val)
    else:
        print("left child: None")
    if root.right:
        print("right child: ", root.right.val)
    else:
        print("right child: None")

    if root.left:
        print_tree_node(root.left)
    if root.right:
        print_tree_node(root.right)

def generate_treenode(input_list, val_idx=0):
    if val_idx >= len(input_list):
        return None

    root = TreeNode(input_list[val_idx])

    left_child_idx = get_left_child_idx(val_idx)
    right_child_idx = get_right_child_idx(val_idx)

    if left_child_idx < len(input_list) and input_list[left_child_idx]:
        root.left = generate_treenode(input_list, left_child_idx)
    if right_child_idx < len(input_list) and input_list[right_child_idx]:
        root.right = generate_treenode(input_list, right_child_idx)

    return root
