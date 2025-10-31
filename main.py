class TreeNode:
    def __init__(self, val:int):
        self.val = val
        self.left=None
        self.right=None


class TreeIter:
    # preorder traversal root,left,right
    # stack holds node,state
    # state=0 current, state=1 left done, state=2 both done
    def __init__(self, root):
        self.root=root
        self.stack=[]
        # history holds the values we've returned so far (in traversal order)
        # next() should return the next item from history instead of advancing the traversal.
        self.history = []
        self.index = -1

    def next(self):
        # If we have gone backwards with prev
        if self.index + 1 < len(self.history):
            self.index += 1
            return self.history[self.index]

        # Otherwise advance the traversal 
        if not self.stack:
            if self.root is None:
                return None
            self.stack.append((self.root,0))
            self.history.append(self.root.val)
            self.index = len(self.history) - 1
            return self.root.val

        while self.stack:
            node,state=self.stack[-1]
            if state==0:
                self.stack[-1]=(node,1)
                if node.left:
                    self.stack.append((node.left,0))
                    self.history.append(node.left.val)
                    self.index = len(self.history) - 1
                    return node.left.val
            elif state==1:
                self.stack[-1]=(node,2)
                if node.right:
                    self.stack.append((node.right,0))
                    self.history.append(node.right.val)
                    self.index = len(self.history) - 1
                    return node.right.val
            else:
                self.stack.pop()
        return None

    def prev(self): 
        if self.index <= 0:
            return None
        self.index -= 1
        return self.history[self.index]




def test_next_return_213():
    root=TreeNode(2)
    left=TreeNode(1)
    right=TreeNode(3)
    left.right=TreeNode(10)
    root.left=left
    root.right=right

    ti=TreeIter(root)
    assert ti.next() == 2
    assert ti.next() == 1
    assert ti.next() == 10
    assert ti.next() == 3
    assert ti.next() is None


test_next_return_213()


def test_prev_and_interleave():
    root=TreeNode(2)
    left=TreeNode(1)
    right=TreeNode(3)
    left.right=TreeNode(10)
    root.left=left
    root.right=right

    ti=TreeIter(root)
    seq=[]
    for _ in range(4):
        seq.append(ti.next())
    assert seq == [2, 1, 10, 3]

    assert ti.prev() == 10
    assert ti.prev() == 1
    assert ti.next() == 10 
    assert ti.prev() == 1
    assert ti.prev() == 2
    assert ti.prev() is None


test_prev_and_interleave()
