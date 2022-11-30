def isPerfect(root):
    def getHeight(root):
        if not root:
            return 0
        return 1 + max(getHeight(root.left),getHeight(root.right))

    def countNodes(root):
        if not root:
            return 0
        return 1 + countNodes(root.left) + countNodes(root.right)

    count = countNodes(root)
    h = getHeight(root)
    return count == 2 ** h - 1
