import unittest
from LCA import LCA
from TreeNode import TreeNode

class TestLCA(unittest.TestCase):

    """
          1
         / \
        2   5
       /   / \
      3   4   6
    """
    def test_lca(self):
        lca = LCA();
        three = TreeNode(3,None,None);
        two = TreeNode(2,three,None);
        four = TreeNode(4,None,None);
        six = TreeNode(6,None,None);
        five = TreeNode(5,four,six);
        root = TreeNode(1,two,five);


        # Test no node
        
        self.assertEqual(None, lca.lowestCommonAncestor(five,three, six));
        imaginary = TreeNode(-1,None,None);
        self.assertEqual(None, lca.lowestCommonAncestor(root,imaginary, six));
        
        # Test available nodes
        self.assertEqual(root, lca.lowestCommonAncestor(root,three, six));
        self.assertEqual(five, lca.lowestCommonAncestor(root,four, six));
        
        # Test node of ancestor
        self.assertEqual(root, lca.lowestCommonAncestor(root,root, six));
        self.assertEqual(five, lca.lowestCommonAncestor(root,five, six));



if __name__ == "__main__":
    unittest.main()



        

        