import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        #test cases
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        
        node3 = TextNode("This is text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.BOLD)

        node5 = TextNode("print('hello world')", TextType.CODE, "https://www.google.com")
        node6 = TextNode("print('hello world')", TextType.CODE, "https://www.google.com")

        node7 = TextNode("some sample text", TextType.IMAGE)
        node8 = TextNode("different sample text", TextType.LINK, "https://www.github.com")

        self.assertEqual(node, node2)
        self.assertNotEqual(node3, node4)
        self.assertEqual(node5, node6)
        self.assertNotEqual(node7, node8)

if __name__ == "__main__":
    unittest.main()