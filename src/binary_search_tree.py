class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        # if the node doesn't have a value yet, set the value
        if not self.val:
            self.val = val
            return

        # if we try to insert a value that already exists, can just return, don't need same thing in there twice
        # so this is a no-op
        if self.val == val:
            return

        # if the given value is less than our node’s value
        if val < self.val:
            # and we already have a left child, then we recursively call insert on our left child
            if self.left:
                self.left.insert(val)
                return

            # if we don’t have a left child yet, then we just make the given value our new left child
            self.left = BSTNode(val)

        # if the given value is greater than our node's value
        if val > self.val:
            # and we already have a right child, then we recursively call insert on the right child
            if self.right:
                self.right.insert(val)
                return

            # if we don't have a right child yet, then we just make the given value our new right child
            self.right = BSTNode(val)

    def get_min(self):
        # set the current node
        current = self
        # traverse the left side of the tree until we hit the node without a left node
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        # set the current node
        current = self
        # traverse the right side until we hit the end
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self is None:
            return self

        if val < self.val:
            self.left = self.left.delete(val)

            return self

        if val > self.val:
            self.right = self.right.delete(val)

            return self

        if self.right is None:
            return self.left

        if self.left is None:
            return self.right

        min_larger_node = self.right

        while min_larger_node.left:
            min_larger_node = min_larger_node.left

        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)

        return self

    def exists(self, val):
        if val == self.val:
            return True

        if val < self.val:
            # at the end on the left side
            if self.val is None:
                return False
            return self.left.exists(val)

        if self.right is None:
            return False
        return self.right.exists(val)

    def inorder(self, vals):
        if self.left is not None:
            self.left.inorder(vals)

        if self.val is not None:
            vals.append(self.val)

        if self.right is not None:
            self.right.inorder(vals)

        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)

        if self.left is not None:
            self.left.preorder(vals)

        if self.right is not None:
            self.right.preorder(vals)

        return vals


def postorder(self, vals):
    if self.left is not None:
        self.left.postorder(vals)

    if self.right is not None:
        self.right.postorder(vals)

    if self.val is not None:
        vals.append(self.val)

    return vals
