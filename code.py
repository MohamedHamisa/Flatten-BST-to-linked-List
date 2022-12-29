 class Solution:
    def flatten(self, root):
        if not root: return
        left, right = root.left, root.right
        self.flatten(left)
        self.flatten(right)
        root.left = None
        if left:
            root.right = left
            while root.right:
                root = root.right
        root.right = right


 '''
The idea is very simple. Suppose n is the current visiting node, and p is the previous node of preorder traversal to n.right.

We just need to do the inorder replacement:

n.left -> NULL

n.right - > n.left

p->right -> n.right
'''
