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


