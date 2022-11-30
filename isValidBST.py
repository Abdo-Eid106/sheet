def isValidBST(root):
    def dfs(root,lower,upper):
        if not root:
            return True
        if root.val <= lower or root.val >= upper:
            return False
        return dfs(root.left,lower,root.val) and dfs(root.right,root.val,upper)

    return dfs(root,float('-infinity'),float('infinity'))