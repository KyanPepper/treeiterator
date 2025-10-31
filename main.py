class TreeNode:
    def __init__(self, val:int):
        self.val = val
        self.left=None
        self.right=None


class TreeIter:
    # preorder traversal root,left,right
    # stack holds node,state
    # state=0 current, state=1 left done, state=2 both done
    #todo use enums or string for readability
    def __init__(self, root):
        self.root=root
        self.stack=[]

    def next(self):
        if not self.stack:
            if self.root is None:
                return None
            self.stack.append((self.root,0))
            return self.root.val

        while self.stack:
            node,state=self.stack[-1]
            if state==0:
                self.stack[-1]=(node,1)
                if node.left:
                    self.stack.append((node.left,0))
                    return node.left.val
            elif state==1:
                self.stack[-1]=(node,2)
                if node.right:
                    self.stack.append((node.right,0))
                    return node.right.val
            else:
                self.stack.pop()
        return None




def test_next_return_213():
    root=TreeNode(2)
    left=TreeNode(1)
    right=TreeNode(3)
    left.right=TreeNode(10)
    root.left=left
    root.right=right

    ti=TreeIter(root)
    print("NEXT:")
    print(ti.next())
    print(ti.next())
    print(ti.next())
    print(ti.next())
    print(ti.next())


test_next_return_213()
