def isSameTree(p, q):
    # 2 edge cases for either true or false 
    # true edge case = borth are empty
    # false edge case = one is empry or values is not equal
    # return recursion 
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
