/* 
Given the root of a binary tree, check whether it is 
a mirror of itself (i.e., symmetric around its center).
*/

var isSymmetric = function (root) {
  function isMirror(t1, t2) {
    if (!t1 && !t2) return true;
    if (!t1 || !t2) return false;
    return (
      t1.val === t2.val &&
      isMirror(t1.left, t2.right) &&
      isMirror(t1.right, t2.left)
    );
  }
  return isMirror(root, root);
};
