class TreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.children = []

def isValidBT(root):
    if not root:
        return True
    if len(root.children) > 2:
        return False
    for child in root.children:
        if not isValidBT(child):
            return False
    return True