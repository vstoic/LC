/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */

// check to see if the root is null
// if it is null return null
// if it is not null then swap the left and right. must set value of left so you dont lose it
// then call the function again on the left and right
// return the root

var invertTree = function (root) {
  if (!root) {
    return null;
  } else {
    let left = root.left;
    root.left = root.right;
    root.right = left;
  }

  invertTree(root.left);
  invertTree(root.right);
  return root;
};
