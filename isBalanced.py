def isBalanced(root):
        def getHeight(root):
            if not root:
                return 0
            return 1 + max(getHeight(root.left),getHeight(root.right))
        
        if not root:
            return True
        if not isBalanced(root.left) or not isBalanced(root.right):
            return False
        return abs(getHeight(root.left) - getHeight(root.right)) <= 1