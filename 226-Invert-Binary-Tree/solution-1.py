def invertTree(root):
    if not root:
        return None
    saved = root.left
    root.left = root.right
    root.right = saved
    invertTree(root.left)
    invertTree(root.right)
    return root