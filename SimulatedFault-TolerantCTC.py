class TreeNode:
    def __init__(self, value=0, children=None):
        self.value = value
        if children is None:
            self.children = []
        else:
            self.children = children

class GeneralTree:
    def __init__(self):
        self.root = None
        self.checkpoint = None

    def insert(self, value, parent=None):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        elif parent:
            parent.children.append(new_node)
        else:
            print("Parent not specified for non-root insertion.")

    def create_checkpoint(self):
        import copy
        self.checkpoint = copy.deepcopy(self.root)
        print("Checkpoint created.")

    def restart_from_checkpoint(self):
        if self.checkpoint:
            self.root = self.checkpoint
            print("Restarted from checkpoint.")
        else:
            print("No checkpoint found.")

    def simulate_failure(self):
        self.root = None
        print("Simulated failure: Tree data lost.")

    def print_tree(self, node, level=0):
        if node is not None:
            print(' ' * 4 * level + '->', node.value)
            for child in node.children:
                self.print_tree(child, level + 1)

# Input: complex tree structure
tree = GeneralTree()
tree.insert(1)  # Root node

# Adding children to the root node
tree.insert(2, tree.root)
tree.insert(3, tree.root)

# Adding children to the first child of the root
tree.insert(4, tree.root.children[0])
tree.insert(5, tree.root.children[0])

# Adding a child to the second child of the root
tree.insert(6, tree.root.children[1])

# Adding more levels
tree.insert(7, tree.root.children[0].children[1])  # Child of node 5

# Output
print("Original tree:")
tree.print_tree(tree.root)
tree.create_checkpoint()
