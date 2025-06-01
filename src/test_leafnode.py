import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        #test cases
        node = LeafNode("p", "Hello, world!")
        print(node.props)
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_link(self):
        node = LeafNode("a", "Click Here!", {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com" target="_blank">Click Here!</a>' )
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
       
if __name__ == "__main__":
    unittest.main()