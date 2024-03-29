
def diameterOfBinaryTree(root):
#   lets have an answer list 
#   using depth first search we have to find 2 things depth and height
#   make sure that if the root is empty / edge case is return 0 
#   figure out which is largr by using max and compare the new depth and old depth. 
#   at the end othe the recursion just return the answer
    answer = [0]
    def dfs(root):
        if not root: return -1
        left = dfs(root.left)
        right = dfs(root.right)
        answer[0] = max(answer[0], 2 + left + right)
        return 1 + max(left, right)
    dfs(root)
    return answer[0]
    